import configparser
from emp.utils.singleton import SingletonMeta
import os


class Config(metaclass=SingletonMeta):
    CONFIG_URL = "../../../config/config.ini"

    def __init__(self) -> None:
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Use the root folder as the base for accessing files and directories
        file_path = os.path.join(script_dir, self.CONFIG_URL)

        try:
            self.config = configparser.ConfigParser()
            self.config.read(file_path)
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

    def get_backup_path(self):
        return self.config['PLAYER']['BACKUP_FOLDER']

    def get_log_level(self):
        return self.config['LOGGER']['LOGLEVEL']

    def get_log_file(self):
        return self.config['LOGGER']['LOGFILE']
