from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.utils.igdb import search_games

router = APIRouter()

@router.get("/games/{query}")
def get_games(query: str):
    try:
        games = search_games(query)
        results = []
        for game in games[:5]:  # Limit to 5 games
            game_info = {
                "name": game.get("name"),
                "cover_url": game.get("cover", {}).get("url")
            }
            results.append(game_info)
        return JSONResponse(content=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
