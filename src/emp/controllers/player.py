from datetime import time
from time import sleep
from emp.controllers.logger import Logger
from emp.models.song import Song
from emp.controllers.status import PlayerStatus
from emp.services.player_service import PlayerService
from emp.utils.singleton import SingletonMeta
import vlc


class Player(metaclass=SingletonMeta):
    logger = Logger()

    def __init__(self, pos, playerService: PlayerService):
        self.pos = pos
        # Create instance of VLC player
        self.player: vlc.MediaPlayer = vlc.MediaPlayer()
        self.playerService: PlayerService = playerService
        self.__backoff = 1

    def play(self):
        next_song: Song = self.playerService.getNext(self.pos)
        player_status = PlayerStatus()
        player_status.metadata = next_song.title + "\n" + \
            next_song.artist.name if next_song.artist is not None else ""

        media = vlc.Media(next_song.url)
        # media = vlc.Media("/test.mp3")
        # Set media to player
        self.player.set_media(media)
        # Play the media

        try:
            self.player.play()
        except Exception:
            self.logger.error("Error playing song {next_song}")
            time.sleep(1)
            self.play()
            
        previous_state = None
        while True:
            state = self.player.get_state()
            if state != previous_state:
                previous_state = state
                self.logger.debug(f"New state: {previous_state}")
                player_status.set_status(state)

            if state == vlc.State.Playing:
                self.__backoff = 1

            if state == vlc.State.Ended:
                self.play()


    def pause(self):
        self.player.pause()
