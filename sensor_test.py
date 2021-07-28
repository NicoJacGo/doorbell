import time
import RPi.GPIO as GPIO

PIN_NUMBER = 12

def listen_for_gpio_change():
    """Continuously listens for state change of GPIO"""
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_NUMBER, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    try:
        while True:
            pin_current = GPIO.input(PIN_NUMBER)
            if pin_current == 1:
                print("circuit open")
            else:
                print("circuit closed")
            while GPIO.input(PIN_NUMBER) == pin_current:
                # waits until the state changes
                time.sleep(0.5)
    except KeyboardInterrupt:
	    GPIO.cleanup()


if __name__ == '__main__':
    listen_for_gpio_change()
