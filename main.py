import RPi.GPIO as gpio
import time
#configurando como BOARD, identificacao fisica dos pino
gpio.setmode(gpio.BOARD)
#configurando a direcao dos pino
gpio.setup(11, gpio.OUT)
print "Setando modo output no pino11 GPIO 17 [LED VERDE]"

gpio.output(11, gpio.HIGH)
print "Led verde acesso"
time.sleep(2)

gpio.output(11, gpio.LOW)
print "led verde apagado"
time.sleep(2)

print

#limpando o gpio
gpio.cleanup()