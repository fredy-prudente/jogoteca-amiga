from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal, init_db
from ..models import CompletedGame, PlayingGame, PlannedGame
from ..schemas import CompletedGame as CompletedGameSchema, PlayingGame as PlayingGameSchema, PlannedGame as PlannedGameSchema, CompletedGameCreate, PlayingGameCreate, PlannedGameCreate
from ..utils.igdb import search_games, get_game_details
import logging

logging.basicConfig(level=logging.INFO)
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/games/{query}")
async def get_games(query: str):
    try:
        games = await search_games(query)
        results = []
        for game in games[:5]:
            game_info = {
                "id": game.get("id"),
                "name": game.get("name"),
                "cover_url": game.get("cover", {}).get("url")
            }
            results.append(game_info)
        return results
    except Exception as e:
        logging.error(f"Error fetching games: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/game_details/{game_id}")
async def get_game_details_route(game_id: int):
    try:
        game_details = await get_game_details(game_id)
        return game_details
    except Exception as e:
        logging.error(f"Error fetching game details: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/library_games/")
def get_library_games(db: Session = Depends(get_db)):
    try:
        completed_games = db.query(CompletedGame).all()
        playing_games = db.query(PlayingGame).all()
        planned_games = db.query(PlannedGame).all()
        return {
            "completed_games": completed_games,
            "playing_games": playing_games,
            "planned_games": planned_games
        }
    except Exception as e:
        logging.error(f"Error fetching library games: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/completed_games/")
def create_completed_game(game: CompletedGameCreate, db: Session = Depends(get_db)):
    try:
        db_game = CompletedGame(**game.dict())
        db.add(db_game)
        db.commit()
        db.refresh(db_game)
        return db_game
    except Exception as e:
        logging.error(f"Error creating completed game: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/playing_games/")
def create_playing_game(game: PlayingGameCreate, db: Session = Depends(get_db)):
    try:
        db_game = PlayingGame(**game.dict())
        db.add(db_game)
        db.commit()
        db.refresh(db_game)
        return db_game
    except Exception as e:
        logging.error(f"Error creating playing game: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/planned_games/")
def create_planned_game(game: PlannedGameCreate, db: Session = Depends(get_db)):
    try:
        db_game = PlannedGame(**game.dict())
        db.add(db_game)
        db.commit()
        db.refresh(db_game)
        return db_game
    except Exception as e:
        logging.error(f"Error creating planned game: {e}")
        raise HTTPException(status_code=500, detail=str(e))
