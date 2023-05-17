from emp.models.song import Song
from emp.repositories.local_player_repository import LocalPlayerRepository
from emp.repositories.player_repository import PlayerRepository
from emp.repositories.remote_player_repository import RemotePlayerRepository
from emp.utils.config import Config
from emp.utils.singleton import SingletonMeta


class PlayerService(metaclass=SingletonMeta):
    repository : PlayerRepository

    def __init__(self) -> None:
        self.config = Config()
        self.base_url = self.config.get_url()
        self.base_path = self.config.get_backup_path()
        pass

    def getNext(self, str) -> Song:
        has_internet: bool = False
        repository =  RemotePlayerRepository(self.base_url) if (has_internet) else LocalPlayerRepository(self.base_path)
        return repository.getNext(str)