from fastapi import FastAPI
from .schemas.user import User
from .schemas.team import Team
# import unicorn
import requests
import json

app = FastAPI()

url = "http://localhost:8000/"

@app.get("/")
async def hello_world():
    return {"hello" : "world"}

@app.get("/users/player_a={idplayer_a}&player_b={idplayer_b}")
async def users(idplayer_a: str, idplayer_b: str):
    ref = url + "users"
    jsonPlayerA = json.loads(requests.get(ref + '/' + idplayer_a).text)
    jsonPlayerB = json.loads(requests.get(ref + '/' + idplayer_b).text)
    data = {
        'iduser': jsonPlayerA.get('id'),
        'displayName': jsonPlayerA.get('displayName'),
        'rank': jsonPlayerA.get('rank'),
        'rankingPoint': jsonPlayerA.get('rankingPoint'),
        'mmr': jsonPlayerA.get('mmr'),
    }
    playerA = User(**data)
    data = {
        'iduser': jsonPlayerB.get('id'),
        'displayName': jsonPlayerB.get('displayName'),
        'rank': jsonPlayerB.get('rank'),
        'rankingPoint': jsonPlayerB.get('rankingPoint'),
        'mmr': jsonPlayerB.get('mmr'),
    }
    playerB = User(**data)

    return {"playerA" : playerA, "playerB" : playerB}

@app.get("/teams")
async def teams():
    return {"hello" : "world"}

if __name__ == "__main__":
    unicorn.run(app, host="127.0.0.1", port=8000)