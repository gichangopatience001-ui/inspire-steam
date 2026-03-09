# Name : Patience Mukuhi Gichango 
#Date : 8/03/2026
# Program to make sensors

from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import network
import urequests
import ujson
import dht
import time
from picozero import Speaker

# OLED size
WIDTH = 128
HEIGHT = 64

# Sensors
sensor = dht.DHT22(Pin(14))
light_sensor = ADC(28)

# Buzzer
speaker = Speaker(15)

# ThingSpeak
API_KEY = "09WFEQ00LOTOTYJ1"
URL = "http://api.thingspeak.com/update"

# WiFi
SSID = "Wokwi-GUEST"
PASSWORD = ""

# OLED setup
i2c = I2C(1, scl=Pin(27), sda=Pin(26))
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# WiFi connection
def connect_wifi():

    oled.fill(0)
    oled.text("Connecting WiFi",10,20)
    oled.show()

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    while not wlan.isconnected():
        time.sleep(1)

    oled.fill(0)
    oled.text("WiFi Connected!",10,20)
    oled.show()
    time.sleep(2)

# Alarm
def alarm():
    speaker.on()
    time.sleep(0.5)
    speaker.off()

# Send data
def send_to_thingspeak(temp, hum, light):

    data = {
        "api_key": API_KEY,
        "field1": temp,
        "field2": hum,
        "field3": light
    }

    response = urequests.post(
        URL,
        data=ujson.dumps(data),
        headers={"Content-Type":"application/json"}
    )

    response.close()

# Startup screen
def startup():

    oled.fill(0)
    oled.text("SMART HOME",25,10)
    oled.text("MONITOR",35,25)
    oled.text("Starting...",25,45)
    oled.show()

    time.sleep(3)

# Main system loop
def system_loop():

    while True:

        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()

        light = light_sensor.read_u16() // 1000

        # Alarm condition
        if temp > 50:
            alarm()

        # Send to cloud
        send_to_thingspeak(temp, hum, light)

        # OLED display
        oled.fill(0)

        oled.text("Home Monitor",15,0)

        oled.text("Temp:",0,20)
        oled.text(str(temp)+"C",60,20)

        oled.text("Hum:",0,35)
        oled.text(str(hum)+"%",60,35)

        oled.text("Light:",0,50)
        oled.text(str(light),60,50)

        oled.show()

        time.sleep(15)

# Run program
startup()
connect_wifi()
system_loop()
