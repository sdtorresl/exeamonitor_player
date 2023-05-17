#!/usr/bin/python3

from datetime import datetime
from threading import Thread, Event
from time import sleep
from emp.controllers.logger import Logger
from emp.controllers.player import Player
from emp.controllers.lcd import LCD
from emp.controllers.display import display
from emp.services.player_service import PlayerService
from emp.utils.config import Config
import RPi.GPIO as GPIO


GPIO.setwarnings(False)
logger = Logger()

def start_play():
    config = Config()
    
    playerService = PlayerService()
    player = Player(config.get_pos_id(), playerService)

    try:
        player.play()
    except Exception as e:
        logger.critical("Critical exception")
        print(e)

def display_info():
    try:
        display()
    except Exception as e:
        lcd = LCD()
        lcd.clear()
        print(e)

if __name__ == '__main__':

    # Create an event object to signal the thread to exit
    Thread(target=start_play, args=()).start()
    Thread(target=display_info, args=()).start()
  