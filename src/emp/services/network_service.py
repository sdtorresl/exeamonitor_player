import netifaces
import requests

from emp.controllers.logger import Logger
from emp.controllers.status import Connectivity, PlayerStatus


class NetworkService():

    @staticmethod
    def get_ipaddress():

        for interface in netifaces.interfaces():
            addrs = netifaces.ifaddresses(interface)
            ip = addrs.get(netifaces.AF_INET)

            if interface.startswith("eth"):
                if ip is not None:
                    ip = ip[0]
                    if "addr" in ip:
                        return "IP: " + ip['addr']

        return ""

    @staticmethod
    def check_internet_connection() -> bool:
        logger = Logger()
        playerStatus: PlayerStatus = PlayerStatus()

        url = "http://www.google.com"
        timeout = 5  # Adjust the timeout value as needed

        try:
            response = requests.head(url, timeout=timeout)
            if response.status_code == 200:
                logger.debug("Internet connection is available.")
                playerStatus.connectivity = Connectivity.ONLINE
                return True
            else:
                logger.warning("Internet connection is not available.")
                playerStatus.connectivity = Connectivity.OFFLINE

        except requests.ConnectionError:
            logger.critical("No internet connection available.")

        return False
