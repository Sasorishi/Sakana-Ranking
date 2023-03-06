from ..schemas.user import User
import requests
import json

url = "http://localhost:8000/"

class UserService():
    # def __init__(self):
    #     print("Users init")

    def getDataMatchs(self, idplayer):
        global url
        request = json.loads(requests.get(url + 'games/ranked/' + idplayer).text)
        return request
    
    def getDataGamepositions(self, data: object):
        stats = {}
        for game in data:
            if game['gameposition'] in stats:
                match game['result']:
                    case "win":
                        value = {"wins": stats[game['gameposition']]['wins'] + 1 }
                        stats[game['gameposition']].update(value)
                    case "defeate":
                        value = {"defeates": stats[game['gameposition']]['defeates'] + 1 }
                        stats[game['gameposition']].update(value)
                    case "draw":
                        value = {"draws": stats[game['gameposition']]['draws'] + 1 }
                        stats[game['gameposition']].update(value)
            else:
                match game['result']:
                    case "win":
                        stats[game['gameposition']] = {
                            'wins': 1,
                            'defeates': 0,
                            'draws': 0
                        }
                    case "defeate":
                        stats[game['gameposition']] = {
                            'wins': 0,
                            'defeates': 1,
                            'draws': 0
                        }
                    case "draw":
                        stats[game['gameposition']] = {
                            'wins': 0,
                            'defeates': 0,
                            'draws': 1
                        }
        return stats

    def getStats(self, idplayer):
        data = self.getDataMatchs(idplayer)
        statsGameposition = self.getDataGamepositions(data)
        if statsGameposition:
            matchs = {
                'wins': 0,
                'defeates': 0,
                'draws': 0
            }
            for match in data:
                if match.get('result') == 'win':
                    matchs['wins'] += 1
                elif match.get('result') == 'defeate':
                    matchs['defeates'] += 1
                elif match.get('result') == 'draw':
                    matchs['draws'] += 1
            matchs['gamepositions'] = statsGameposition
        else:
            matchs = {
                'wins': 0,
                'defeates': 0,
                'draws': 0,
            }
            for match in data:
                if match.get('result') == 'win':
                    matchs['wins'] += 1
                elif match.get('result') == 'defeate':
                    matchs['defeates'] += 1
                elif match.get('result') == 'draw':
                    matchs['draws'] += 1

        return matchs

    def getData(self, idplayer):
        global url
        request = json.loads(requests.get(url + 'users/' + idplayer).text)
        matchs = self.getStats(idplayer)
        data = {
            'iduser': request.get('id'),
            'displayName': request.get('displayName'),
            'rank': request.get('rank'),
            'division': request.get('division'),
            'rankPoints': request.get('rankPoints', 0),
            'matchs': matchs
        }
        player = User(**data)
        return player
    
    def getAllUsersId(self):
        global url
        request = json.loads(requests.get(url + 'users/').text)
        return request