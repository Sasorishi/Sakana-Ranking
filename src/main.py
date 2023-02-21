from fastapi import FastAPI, Request, Body, Response
from .schemas.team import Team
from .services.ranking import RankingService
from .services.user import UserService
from .services.request import RequestService

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"hello" : "world"}

# 3wZmHSYmEvfzZWJ5qGRbxtF63Kp2
# 2iraTWotVKg3DBmg8k2UvBzEuXB3
# e2aX0MOs26TMRmMztaRsOb57CY22

@app.post("/users/set_rank")
async def users(request: object = Body(...)):
    rankingService = RankingService()
    userService = UserService()
    requestService = RequestService()
    playerA = userService.getData(request['idplayer_a'])
    playerB = userService.getData(request['idplayer_b'])
    points = rankingService.getRankPoint(playerA, playerB, request['score'])

    requestService.setRank(request['idplayer_a'], points['playerA'])
    requestService.setRank(request['idplayer_b'], points['playerB'])
    return {"playerA" : points['playerA'], "playerB" : points['playerB']}

@app.post("/users/reset_rank")
async def users(request: object = Body(...)):
    requestService = RequestService()
    requestService.resetRank(request['idplayer_a'])
    requestService.resetRank(request['idplayer_b'])
    return {"Success" : "reset rank"}

@app.get("/teams")
async def teams():
    return {"hello" : "world"}

@app.get("/test/{idplayer}")
async def update(idplayer: str):
    requestService = RequestService()
    params = {
        'rank': 'Bronze',
        'division': '4',
        'rankPoints': 24
    }
    requestService.setRank(idplayer, params)
    return {"hello" : "world"}


@app.post("/test", status_code=201)
async def test(request: Request, response: Response, test: object = Body(...)):
    return await request.body()
    #     if request:
    #         return await request.body()
    #     else:
    #         return {"Error" : "Request cannot be empty"}
    # return {"Request" : "Waiting for request"}

if __name__ == "__main__":
    unicorn.run(app, host="127.0.0.1", port=8000)