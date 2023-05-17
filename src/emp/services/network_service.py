import netifaces
import requests

from emp.controllers.logger import Logger

class NetworkService():


    @staticmethod
    def get_ipaddress():

        for interface in netifaces.interfaces():
            addrs = netifaces.ifaddresses(interface)
            ip = addrs.get(netifaces.AF_INET)

            if interface.startswith("eth"):
                return "IP: " + ip[0]['addr']

        return None


    @staticmethod
    def check_internet_connection() -> bool:
        logger = Logger()

        url = "http://www.google.com"
        timeout = 5  # Adjust the timeout value as needed

        try:
            response = requests.head(url, timeout=timeout)
            if response.status_code == 200:
                logger.debug("Internet connection is available.")
                return True
            else:
                logger.warning("Internet connection is not available.")
        except requests.ConnectionError:
            logger.critical("No internet connection available.")

        return False
