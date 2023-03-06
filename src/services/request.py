import requests
import json

url = "http://localhost:8000/"

class RequestService():
    # def __init__(self):
    #     print("Users init")

    def setRank(self, idplayer: str, params: object, ref: str):
        global url
        uri = f"{ref}/update/rank/{idplayer}"
        rank = params['rank']
        division = params['division']
        rankPoints = params['rankPoints']

        payload = f'rank={rank}&division={division}&rankPoints={rankPoints}'
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("PUT", url + uri, headers=headers, data=payload)
        print(response.text)

    def setDataInSeason(self, idseason: str, params: object, ratio: float):
        global url
        uri = f"leagues/update/rank/{idseason}/{params.iduser}"
        rank = params.rank
        division = params.division
        rankPoints = params.rankPoints
        wins = params.matchs['wins']
        defeates = params.matchs['defeates']
        draws = params.matchs['draws']

        if 'gamepositions' in params.matchs:
            gamepositions = params.matchs['gamepositions']
            data = {
                "rank": rank,
                "division": division,
                "rankPoints": rankPoints,
                "wins": wins,
                "defeates": defeates,
                "draws": draws,
                "ratio": ratio,
                "gamepositions": gamepositions
            }
            payload = json.dumps(data)
        else:
            data = {
                "rank": rank,
                "division": division,
                "rankPoints": rankPoints,
                "wins": wins,
                "defeates": defeates,
                "draws": draws,
                "ratio": ratio
            }
            payload = json.dumps(data)
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("PUT", url + uri, headers=headers, data=payload)
        print(response.text)

    def resetRank(self, idplayer: str, ref: str):
        global url
        uri = f"{ref}/update/rank/{idplayer}"
        rank = 'Unranked'
        division = 'Unranked'
        rankPoints = 0

        payload = f'rank={rank}&division={division}&rankPoints={rankPoints}'
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("PUT", url + uri, headers=headers, data=payload)
        print(response.text)
