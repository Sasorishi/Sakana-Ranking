from pydantic import BaseSettings

class Settings(BaseSettings):
    divisionPoint: int = 72
    gainPoint: int = 18
    lostPoint: int = 12
    brake: int = 50
    bronze: list = [24, 96, 168, 240]
    silver: list = [312, 384, 456, 528]
    gold: list = [600, 672, 744, 816]
    platinium: list = [888, 960, 1032, 1104]
    diamond: list = [1176, 1248, 1320, 1392]
    champion: list = [1464, 1536, 1608, 1680]
    sakana: list = [1752]