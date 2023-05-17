import json
import requests
from emp.controllers.logger import Logger
from emp.repositories.player_repository import PlayerRepository
from emp.utils.singleton import SingletonMeta
from emp.models.song import Song

class RemotePlayerRepository(PlayerRepository):
    logger = Logger()

    def __init__(self, base_url):
        self.base_url = base_url

    def getNext(self, pos) -> Song:
        endpoint = self.base_url + "/player/next/" + str(pos) + ".json?cached=false"
        jsonResponse = requests.request("GET", endpoint)
        response = json.loads(jsonResponse.text)
        self.logger.debug(response)
        return Song.from_dict(response)
