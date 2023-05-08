#!/usr/bin/python3

from datetime import datetime
from threading import Thread
from time import sleep
from emp.controllers.player import Player
from emp.repositories.player_repository import PlayerRepository
from emp.controllers.lcd import LCD
from emp.controllers.display import display
from emp.utils.config import Config


def start_play():
    try:
        config = Config()
        playerRepository = PlayerRepository(config.get_url())
        player = Player(config.get_pos_id(), playerRepository)
        player.play()
    except KeyboardInterrupt:
        lcd = LCD()
        lcd.clear()
        print("bye")

def display_info():
    display()

if __name__ == '__main__':
    
    Thread(target=start_play, args=()).start()
    Thread(target=display_info, args=()).start()
    #Thread(target=main, args=()).start()
    #Thread(target=stateoff, args=()).start()
    #Thread(target=stateon, args=()).start()
    #Thread(target=checkSoundOutput, args=()).start()
    #Thread(target=buttons, args=()).start()
