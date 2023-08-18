import json
import requests
import base64
from emp.controllers.logger import Logger
from emp.repositories.player_repository import PlayerRepository
from emp.utils.singleton import SingletonMeta
from emp.models.song import Song

class RemotePlayerRepository(PlayerRepository):
    logger = Logger()

    def __init__(self, base_url, user):
        self.base_url = base_url
        self.user = base64.b64encode(user.encode("ascii"))

    def getNext(self, pos):
        Headers = { 
          "Content-Type" : "application/json",
          "X-USER-TOKEN" : self.user
        }
        endpoint = self.base_url + "/player/next/" + str(pos)
        jsonResponse = requests.get(endpoint, headers = Headers)
        response = json.loads(jsonResponse.text)
        self.logger.debug(response);
        self.logSong(response['payload'], pos)
        return response['payload']['song'];

    def logSong(self, response, pos):
        fromObject = {
          "title": response['song']['name'],
          "author": response['song']['artist'],
          "song_id": response['song']['self']['id'],
          "pos_id": pos,
          "rule_id": response['ruleId']
        }
        endpoint = self.base_url+"/song/history";
        
        Headers = { 
          "Content-Type" : "application/json",
          "X-USER-TOKEN" : self.user
        }
        jsonResponse = requests.post(endpoint, data=json.dumps(fromObject), headers = Headers)
        return jsonResponse
