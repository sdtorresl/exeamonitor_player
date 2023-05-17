from emp.models.song import Song
from emp.utils.singleton import SingletonMeta

class PlayerRepository(metaclass=SingletonMeta):
    def get_next(self, str) -> Song:
        """Get next song."""
        pass
