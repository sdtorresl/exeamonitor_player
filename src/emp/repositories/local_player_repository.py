import json
import requests
from emp.controllers.logger import Logger
from emp.repositories.player_repository import PlayerRepository
from emp.utils.singleton import SingletonMeta
from emp.models.song import Artist, Song
import os
import random
from mutagen.mp3 import MP3

class LocalPlayerRepository(PlayerRepository):
    logger = Logger()

    def __init__(self, path):
        self.path = path
        self.logger.info("Path: " +self.path)


    def getNext(self, pos) -> Song:
        mp3_files = self.find_mp3_files(self.path)
        url = random.choice(mp3_files)
        self.logger.info(url)

        # Load the MP3 file
        mp3 = MP3(url)

        # Access the metadata
        title = mp3.get('title') if mp3.get('title') is not None else ""
        artist = mp3.get('artist') if mp3.get('artist') is not None else ""
        album = mp3.get('album') if mp3.get('album') is not None else ""

        return Song(id="", title=title, name=title, url=url, artist=Artist(name=artist), art="")
    
    
    def find_mp3_files(self, folder):
        mp3_files = []

        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.lower().endswith('.mp3'):
                    mp3_files.append(os.path.join(root, file))

        return mp3_files


