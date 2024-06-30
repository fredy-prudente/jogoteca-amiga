from pydantic import BaseModel
from datetime import date

class CompletedGameBase(BaseModel):
    game_id: int
    game_name: str
    platform: str
    start_date: date
    end_date: date
    rating: int

class CompletedGameCreate(CompletedGameBase):
    pass

class CompletedGame(CompletedGameBase):
    id: int

    class Config:
        from_attributes = True  
