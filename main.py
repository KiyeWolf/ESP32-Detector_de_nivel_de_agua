import machine
import time
from machine import Pin,PWM
from machine  import Pin
import tm1637
from tm1637 import TM1637
from hcsr04  import HCSR04


display=TM1637(clk=Pin(4),  dio=Pin(0))
sensor=HCSR04(trigger_pin=26, echo_pin=27)
pwmServo = PWM(Pin(15,Pin.OUT))
pwmServo.freq(50)
inicio=0000
display.number(inicio)
while True:
    distancia=sensor.distance_cm()
    print('distancia:',distancia,'cm') 
    display.number(int(distancia))
    time.sleep(2)
    pwmServo.duty(25)
    time.sleep(3)
    pwmServo.duty(125)
    time.sleep(2)
   
