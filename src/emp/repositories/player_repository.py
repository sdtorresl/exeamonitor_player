import json
import requests
from emp.utils.singleton import SingletonMeta
from emp.models.song import Song

class PlayerRepository(metaclass=SingletonMeta):

    def __init__(self, base_url):
        self.base_url = base_url

    def getNext(self, pos) -> Song:
        endpoint = self.base_url + "/player/next/" + str(pos) + ".json?cached=false"
        jsonResponse = requests.request("GET", endpoint)
        response = json.loads(jsonResponse.text)
        return Song.from_dict(response)


