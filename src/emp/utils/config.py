import configparser
from emp.utils.singleton import SingletonMeta


class Config(metaclass=SingletonMeta):
    CONFIG_URL = "../config/config.ini"

    def __init__(self) -> None:
        try:
            self.config = configparser.ConfigParser()
            self.config.read(self.CONFIG_URL)
        except:
            print('Unable to read config file ${CONFIG_FILE}')

    def get_url(self):
        return self.config['SERVER']['URL']
    
    def get_pos_id(self):
        return self.config['PLAYER']['POSID']

    def get_title(self):
        return self.config['PLAYER']['TITLE']
    
    def get_serial(self):
        return self.config['PLAYER']['SERIAL']
    
    def get_brand(self):
        return self.config['PLAYER']['BRAND']
