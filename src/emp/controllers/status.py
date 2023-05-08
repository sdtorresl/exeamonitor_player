from emp.utils.singleton import SingletonMeta
from enum import Enum
import vlc

class Status(Enum):
    PLAYING = 'Reproduciendo'
    STOPPED = 'Detenido'
    OPENING = 'Abriendo'
    PAUSED = 'Pausado'
    UNKNOWN = 'Desconocido'

class PlayerStatus(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.status = None
        self.metadata = None

    def get_status(self):
        return str(self.status.value) if self.status is not None else ""
    
    def set_status(self, status):
        if status == vlc.State.Opening:
            self.status = Status.OPENING
        if status == vlc.State.Playing:
            self.status = Status.PLAYING
        if status == vlc.State.Stopped or status == vlc.State.Paused:
            self.status = Status.STOPPED
        if status == vlc.State.Stopped:
            self.status = Status.STOPPED
        else:
            self.status = Status.UNKNOWN
            