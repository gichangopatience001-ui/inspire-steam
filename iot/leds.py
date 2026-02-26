#Name : Patience Mukuhi Gichango 
#Date : 26/02/2026
# Program to blink leds

from machine import Pin

import time

red_led = Pin(28, Pin.OUT) 
yellow_led = Pin(27, Pin.OUT) 
while True:
    red_led.on()
    yellow_led.off()
    time.sleep(1) # Wait for USB to become ready
    red_led.off()
    yellow_led.on()
    time.sleep(1) # Wait for USB to become ready
    print("Learnimg IOT.") 