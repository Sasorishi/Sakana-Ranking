from pydantic import BaseModel

class Team(BaseModel):
    idteam: str
    name: str
    rank: str
    rankingPoint: float
    eloPoint: float

