from .settings import Settings

class RankingService():
    def __init__(self):
        self.settings = Settings()

    def isRankedAccess(self, matchs: int):
        if matchs >= 10:
            return True
        return False

    def isChangeDivision(self, value: int, player_rank: str):
        indice = 5
        match player_rank:
            case 'Unranked':
                if value >= self.settings.bronze[0]:
                    return len(self.settings.bronze)
                else:
                    return 'Unranked'
            case 'Bronze':
                for division in self.settings.bronze:
                    if value >= division:
                        indice -= 1
            case 'Silver':
                for division in self.settings.silver:
                    if value >= division:
                        indice -= 1
            case 'Gold':
                for division in self.settings.gold:
                    if value >= division:
                        indice -= 1
            case 'Platinium':
                for division in self.settings.platinium:
                    if value >= division:
                        indice -= 1
            case 'Diamond':
                for division in self.settings.diamond:
                    if value >= division:
                        indice -= 1
            case 'Champion':
                for division in self.settings.champion:
                    if value >= division:
                        indice -= 1
        return indice - 1

    def isChangeRank(self, value: int, player_rank: str):
        match player_rank:
            case 'Unranked':
                if value >= self.settings.bronze[0]:
                    return 'Bronze'
            case 'Bronze':
                if value >= self.settings.silver[0]:
                    return 'Silver'
            case 'Silver':
                if value >= self.settings.gold[0]:
                    return 'Gold'
                if value <= self.settings.silver[0]:
                    return 'Bronze'
            case 'Gold':
                if value >= self.settings.platinium[0]:
                    return 'Platinium'
                if value <= gold[0]:
                    return 'Silver'
            case 'Platinium':
                if value >= self.settings.champion[0]:
                    return 'Champion'
                if value <= self.settings.platinium[0]:
                    return 'Gold'
            case 'Champion':
                if value >= self.settings.sakana[0]:
                    return 'Sakana League'
                if value <= self.settings.champion[0]:
                    return 'Platinium'
            case 'Sakana League':
                if value <= self.settings.sakana[0]:
                    return 'Champion'
        return player_rank

    def unfairGame(self, diffDivision: float, rankPoints: int):
        if diffDivision == 0:
            rankPoints += self.settings.gainPoint
            print(f"FairGame: {rankPoints} += {self.settings.gainPoint}")
        elif diffDivision == 1:
            rankPoints += (self.settings.gainPoint - 6)
            print(f"FairGame: {rankPoints} += ({self.settings.gainPoint} - 6)")
        elif diffDivision == 2:
            rankPoints += (self.settings.gainPoint - 10)
            print(f"FairGame: {rankPoints} += ({self.settings.gainPoint} - 10)")
        elif diffDivision >= 3:
            rankPoints += 0
            print(f"FairGame: {rankPoints} += 0")

        print(f"DiffDivision {diffDivision}")
        return rankPoints

    def calcDiffDivision(self, divisionA: int, divisionB: int, playerA: object, playerB: object):
        division = 0
        if playerA.rank != playerB.rank:
            division = (playerA.rankPoints - playerB.rankPoints) / 72
            division = round(division)
            print(f"{playerA.rankPoints} - {playerB.rankPoints} / 72 = {division}")
        else:
            division = int(divisionA) - int(divisionB)
            print(f"{divisionA} - {divisionB} = {division}")

        return division
    
    def getDiffDivision(self, playerA: object, playerB: object):
        if playerA.division == 'Unranked':
            a = 4
        else:
            a = playerA.division
        if playerB.division == 'Unranked':
            b = 4
        else:
            b = playerB.division

        if playerA.rankPoints < playerB.rankPoints:
            division = self.calcDiffDivision(a, b, playerA, playerB)
        else:
            division = self.calcDiffDivision(b, a, playerA, playerB)
        return division

    def getRatio(self, wins: int, defeates: int):
        try:
            ratio = wins/defeates
        except ZeroDivisionError:
            ratio = 0
        return ratio

    def multiplicationPoint(self, division: int):
        gain = self.settings.gainPoint
        lost = self.settings.lostPoint
        print(f"Before: {gain}")
        match division:
            case 1:
                gain *= 2
                lost *= 2
            case 2:
                gain *= 3
                lost *= 3
            case 3:
                gain *= 4
                lost *= 4
            case 4:
                gain *= 5
                lost *= 5
            case 5:
                gain *= 6
                lost *= 6
            case 0:
                gain
                lost
        print(f"After: {gain}")
        result = {
            'gainPoint': gain,
            'lostPoint': lost,
        }        
        return result

    def winstreak(self, rankPoint: list, wins: int, defeates: int, draws: int):
        ratio = self.getRatio(wins, defeates)
        matchs = wins + defeates + draws
        if matchs >= self.settings.brake:
            rankPoint['lostPoint'] -= 2
            if ratio >= 1.2:
                rankPoint['gainPoint'] += 6
            elif ratio >= 1.1:
                rankPoint['gainPoint']
            else:
                rankPoint['gainPoint'] -= 6
        results = {
            'gainPoint': rankPoint['gainPoint'],
            'lostPoint': rankPoint['lostPoint'],
        }   
        return results

    def calcResult(self, playerA: object, playerB: object, result: str, pointsA: list, pointsB: list, diffDivision: int):
        match result:
            case 'a':
                playerB.rankPoints -= pointsB['lostPoint']
                if playerB.rankPoints <= 0:
                    playerB.rankPoints = 0              
                if playerA.rankPoints > playerB.rankPoints:
                    print(f"{playerA.rankPoints} > {playerB.rankPoints}")
                    playerA.rankPoints = self.unfairGame(diffDivision, playerA.rankPoints)
                else:
                    print(f"Calc: {playerA.rankPoints} += {pointsA['gainPoint']}")
                    playerA.rankPoints += pointsA['gainPoint']

            case 'b':
                playerA.rankPoints -= pointsB['lostPoint']
                if playerA.rankPoints <= 0:
                    playerA.rankPoints = 0
                if playerB.rankPoints > playerA.rankPoints:
                    playerB.rankPoints = self.unfairGame(diffDivision, playerB.rankPoints)
                else:
                    playerB.rankPoints += pointsB['gainPoint']
            case 'drawn':
                playerA.rankPoints
                playerB.rankPoints
        results = {
            'a': playerA.rankPoints,
            'b': playerB.rankPoints,
        }
        return results

    def getRankPoint(self, playerA: object, playerB: object, result: str):
        print(f"Player a: {playerA}")
        print(f"Player b: {playerB}")
        diffDivision = self.getDiffDivision(playerA, playerB)
        multiplicationPoint = self.multiplicationPoint(diffDivision)
        pointsA = self.winstreak(multiplicationPoint, playerA.matchs['wins'], playerA.matchs['defeates'], playerA.matchs['draws'])
        pointsB = self.winstreak(multiplicationPoint, playerB.matchs['wins'], playerB.matchs['defeates'], playerB.matchs['draws'])
        rankPoints = self.calcResult(playerA, playerB, result, pointsA, pointsB, diffDivision)
        rankA = self.isChangeRank(rankPoints['a'], playerA.rank)
        rankB = self.isChangeRank(rankPoints['b'], playerB.rank)
        divisionA = self.isChangeDivision(rankPoints['a'], rankA)
        divisionB = self.isChangeDivision(rankPoints['b'], rankB)

        playersData = {
            'playerA': {
                'rank' : rankA,
                'division': divisionA,
                'rankPoints': rankPoints['a'],
            },
            'playerB': {
                'rank' : rankB,
                'division': divisionB,
                'rankPoints': rankPoints['b']
            }
        }

        return playersData
        

# def antiCheat():
    # fraude date soir
    # fraude meme personne

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