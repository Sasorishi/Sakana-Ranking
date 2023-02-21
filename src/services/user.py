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

    def getStats(self, idplayer):
        data = self.getDataMatchs(idplayer)
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
            'matchs': {
                'wins': matchs['wins'],
                'defeates': matchs['defeates'],
                'draws': matchs['draws'] 
            }
        }
        player = User(**data)
        return player
    
    # def setRankPoint():