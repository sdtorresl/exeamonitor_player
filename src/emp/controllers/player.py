from time import sleep
from emp.models.song import Song
from emp.repositories.player_repository import PlayerRepository
from emp.controllers.status import PlayerStatus
from emp.utils.singleton import SingletonMeta
import vlc


class Player(metaclass=SingletonMeta):
    def __init__(self, pos, playerRepository: PlayerRepository):
        self.pos = pos
        # Create instance of VLC player
        self.player: vlc.MediaPlayer = vlc.MediaPlayer()
        self.playerRepository: PlayerRepository = playerRepository
        self.__backoff = 1

    def play(self):
        next_song: Song = self.playerRepository.getNext(self.pos)
        player_status = PlayerStatus()
        player_status.metadata = next_song.title + "\n" + \
            next_song.artist.name if next_song.artist is not None else ""

        media = vlc.Media(next_song.url)
        # media = vlc.Media("/test.mp3")
        # Set media to player
        self.player.set_media(media)
        # Play the media

        self.player.play()
        previous_state = None
        while True:
            state = self.player.get_state()
            if state != previous_state:
                previous_state = state
                print(previous_state)
                player_status.set_status(state)

            if state == vlc.State.Playing:
                self.__backoff = 1

            if state == vlc.State.Ended:
                self.play()


    def pause(self):
        self.player.pause()
