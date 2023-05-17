from emp.utils.singleton import SingletonMeta
from enum import Enum
import vlc


class Status(Enum):
    PLAYING = 'Reproduciendo'
    STOPPED = 'Detenido'
    OPENING = 'Abriendo'
    PAUSED = 'Pausado'
    UNKNOWN = 'Desconocido'


class Connectivity(Enum):
    ONLINE = "En linea"
    OFFLINE = "Desconectado"


class PlayerStatus(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self._status = None
        self.metadata = None
        self._connectivity = Connectivity.ONLINE

    def get_status(self):
        return str(self._status.value) if self._status is not None else ""

    def set_status(self, status):
        if status == vlc.State.Opening:
            self._status = Status.OPENING
        if status == vlc.State.Playing:
            self._status = Status.PLAYING
        if status == vlc.State.Stopped or status == vlc.State.Paused:
            self._status = Status.STOPPED
        if status == vlc.State.Stopped:
            self._status = Status.STOPPED
        else:
            self._status = Status.UNKNOWN

    @property
    def connectivity(self):
        return self._connectivity

    @connectivity.setter
    def connectivity(self, conn_status):
        if isinstance(conn_status, Connectivity):
            self._connectivity = conn_status
        else:
            raise ValueError(
                "Invalid value for connectivity. Expected Connectivity.")
