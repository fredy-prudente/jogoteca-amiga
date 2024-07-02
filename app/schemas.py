from pydantic import BaseModel
from datetime import date

class CompletedGameBase(BaseModel):
    game_id: int
    game_name: str
    platform: str
    start_date: date
    end_date: date
    rating: int
    cover_url: str

class CompletedGameCreate(CompletedGameBase):
    pass

class CompletedGame(CompletedGameBase):
    id: int

    class Config:
        from_attributes = True

class PlayingGameBase(BaseModel):
    game_id: int
    game_name: str
    platform: str
    start_date: date
    cover_url: str

class PlayingGameCreate(PlayingGameBase):
    pass

class PlayingGame(PlayingGameBase):
    id: int

    class Config:
        from_attributes = True

class PlannedGameBase(BaseModel):
    game_id: int
    game_name: str
    platform: str
    cover_url: str

class PlannedGameCreate(PlannedGameBase):
    pass

class PlannedGame(PlannedGameBase):
    id: int

    class Config:
        from_attributes = True
