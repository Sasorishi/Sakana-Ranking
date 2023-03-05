from .settings import Settings
import time
from datetime import datetime, timedelta, date

class AntiCheatService():
    def __init__(self):
        self.settings = Settings()

    def checkDatetime(self, timestamp: int):
        result = datetime.fromtimestamp(int(timestamp))
        if result.hour <= self.settings.sundown and result.hour >= self.settings.sunrise:
            return True
        return False

    def checkSameOpponent(self, matchs: object, playerA: str, playerB: str):
        # 1 semaine de diff evite le PL
        result = datetime.fromtimestamp(timestamp)
        expiredays = result + datetime.timedelta(days = self.settings.reloaddays)
        array = None
        # for match in matchs:
        #     if match.hostId == player or match.
        return False
    
    def softBanAccount(self):
        return True
    
    def detectCheat(self, timestamp: int):
        if self.checkDatetime(timestamp):
            return True
        # self.checkSameOpponent()
        return False