## Video 04 - Subroutines

from machine import Pin
from time import sleep

LED = Pin(16, Pin.OUT)
LED2 = Pin(25, Pin.OUT)



for i in range(0, 10):
    LED.toggle()
    LED2.toggle()
    sleep(0.5)

LED.value(0)
LED2.value(0)
