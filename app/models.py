from sqlalchemy import Column, Integer, String, Date
from .database import Base

class CompletedGame(Base):
    __tablename__ = 'completed_games'
    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, index=True)  
    game_name = Column(String, index=True)
    platform = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    rating = Column(Integer)
