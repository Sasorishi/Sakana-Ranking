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
    
    def gamepositions(self, data: object):
        stats = {}
        if hasattr(data, 'gamepositions'):
            stats[data.gamepositions] = {
                'wins': 0,
                'defeates': 0,
                'draws': 0
            }       
        return stats

    def getStats(self, idplayer):
        data = self.getDataMatchs(idplayer)
        statsGameposition = self.gamepositions(data)
        if statsGameposition != None:
            matchs = {
                'wins': 0,
                'defeates': 0,
                'draws': 0
            }
            matchs['gamepositions'] = statsGameposition
            for match in data:
                if match.get('result') == 'win':
                    matchs['wins'] += 1
                    statsGameposition['wins'] += 1
                elif match.get('result') == 'defeate':
                    matchs['defeates'] += 1
                    statsGameposition['defeates'] += 1
                elif match.get('result') == 'draw':
                    matchs['draws'] += 1
                    statsGameposition['draws'] += 1
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