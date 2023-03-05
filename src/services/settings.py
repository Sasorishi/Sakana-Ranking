from pydantic import BaseSettings

class Settings(BaseSettings):
    divisionPoint: int = 72
    gainPoint: int = 18
    lostPoint: int = 12
    brake: int = 30

    bronze: list = [24, 96, 168, 240]
    silver: list = [312, 384, 456, 528]
    gold: list = [600, 672, 744, 816]
    platinium: list = [888, 960, 1032, 1104]
    diamond: list = [1176, 1248, 1320, 1392]
    champion: list = [1464, 1536, 1608, 1680]
    sakana: list = [1752]

    sunrise: int = 5
    sundown: int = 3
    reloaddays: int = 7

# bo3
# 72 = 4 wins
# 18
# 12

# 4 fois wins pour monter
# 6 fois loses pour descendre
# 5O wins de suites pour être platinum 3
# 36-2 24-3 18-4 12-6 

# Sakana League
# Champion 1 2300 1680
# Champion 2
# Champion 3
# Champion 4 2100
# Diamond 1 2099
# Diamond 2
# Diamond 3
# Diamond 4 1750 1176
# Platnium 1 1749 1104
# Platinum 2 * 1032
# Platinum 3 * 960
# Platinum 4 1550 888
# Gold 1 1549 816
# Gold 2 * 744
# Gold 3 * 672
# Gold 4 1350 600
# Fer 1 1399 528
# Fer 2 * 456
# Fer 3 * 384
# Fer 4 1150 312
# Bronze 1 1149 240
# Bronze 2 1049 168
# Bronze 3 949 96
# Bronze 4 849 24
# Unranked 849