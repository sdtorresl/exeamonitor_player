from datetime import datetime
from time import sleep
from emp.controllers.lcd import LCD
from emp.controllers.logger import Logger
from emp.controllers.status import PlayerStatus
from emp.services.network_service import NetworkService
from emp.utils.config import Config


def display():
    lcd = LCD()
    logger = Logger()
    network_service: NetworkService = NetworkService()

    try:
        config: Config = Config()
        player_status: PlayerStatus = PlayerStatus()

        # logger.info('Player started!')

        lcd.clear()
        lcd.begin(16, 1)
        # Start the main program in an infinite loop
        while True:
            # status = run_cmd(cmd_check_device, True)
            # status = status[:4]
            lcd.clear()
            lcd.message(config.get_brand() + "\n")
            if player_status.connectivity is not None:
                lcd.message(f"{player_status.connectivity.value}")
            sleep(2)

            lcd.clear()
            lcd.message("Escuchas:\n")
            lcd.message(config.get_title())
            sleep(2)

            if player_status.metadata is not None:
                lcd.clear()
                lcd.message(player_status.metadata)
                sleep(2)

            # Show Serial
            lcd.clear()
            lcd.message("Serial:\n")
            lcd.message(config.get_serial())
            sleep(3)

            # Show IP info
            lcd.clear()
            ipaddr = network_service.get_ipaddress()

            if not ipaddr:
                lcd.message('Sin Internet\n')
            else:
                lcd.message(ipaddr + "\n")

            # Show date for 10 seconds
            i = 0
            while i < 3:
                lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
                sleep(1)
                i = i+1
                pass
    except Exception as e:
        lcd.clear()
        logger.critical(e)
        raise e
        display()
