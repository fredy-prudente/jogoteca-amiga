from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal, init_db
from ..models import CompletedGame
from ..schemas import CompletedGameCreate, CompletedGame as CompletedGameSchema
from ..utils.igdb import search_games, get_game_details
import logging

logging.basicConfig(level=logging.INFO)
router = APIRouter()

# Dependency to get DB session
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
        for game in games[:5]:  # Limit to 5 games
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

@router.post("/completed_games/", response_model=CompletedGameSchema)
def create_completed_game(game: CompletedGameCreate, db: Session = Depends(get_db)):
    try:
        logging.info(f"Received game data: {game}")
        db_game = CompletedGame(
            game_name=game.game_name,
            platform=game.platform,
            start_date=game.start_date,
            end_date=game.end_date,
            rating=game.rating
        )
        db.add(db_game)
        db.commit()
        db.refresh(db_game)
        logging.info(f"Game saved with ID: {db_game.id}")
        return db_game
    except Exception as e:
        logging.error(f"Error saving game: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/completed_games/", response_model=list[CompletedGameSchema])
def read_completed_games(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        games = db.query(CompletedGame).offset(skip).limit(limit).all()
        logging.info(f"Retrieved games: {games}")
        return games
    except Exception as e:
        logging.error(f"Error reading completed games: {e}")
        raise HTTPException(status_code=500, detail=str(e))
