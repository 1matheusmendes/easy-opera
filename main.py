import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

gpio.setup(11, gpio.OUT)

while True
gpio.output(11, gpio.HIGH)
time.sleep(2)
gpio.outout(11, gpio.LOW)
time.sleep(2)

gpio.cleanup()