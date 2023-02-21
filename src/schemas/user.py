from pydantic import BaseModel, validator
from typing import Optional

class User(BaseModel):
    iduser: str
    displayName: str
    rank: str | Optional[str] = ''
    division: str | Optional[str] = ''
    rankPoints: int | Optional[int] = ''
    matchs: object

    class Config:
        validate_assignment = True

    @validator('rank')
    def set_rank(cls, rank):
        return rank or 'Unranked'
    
    @validator('division')
    def set_division(cls, division):
        return division or 'Unranked'
    
    @validator('rankPoints')
    def set_rankPoints(cls, rankPoints):
        return rankPoints or 0

