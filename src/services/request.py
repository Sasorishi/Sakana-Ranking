import requests

url = "http://localhost:8000/"

class RequestService():
    # def __init__(self):
    #     print("Users init")

    def setRank(self, idplayer: str, params: object):
        global url
        uri = f"users/update/rank/{idplayer}"
        rank = params['rank']
        division = params['division']
        rankPoints = params['rankPoints']

        payload = f'rank={rank}&division={division}&rankPoints={rankPoints}'
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("PUT", url + uri, headers=headers, data=payload)
        print(response.text)

    def resetRank(self, idplayer: str):
        global url
        uri = f"users/update/rank/{idplayer}"
        rank = 'Unranked'
        division = 'Unranked'
        rankPoints = 0

        payload = f'rank={rank}&division={division}&rankPoints={rankPoints}'
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("PUT", url + uri, headers=headers, data=payload)
        print(response.text)
