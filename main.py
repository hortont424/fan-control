import Adafruit_DHT as DHT
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

fan_relay_channel = 27
sensor_channel = 17

GPIO.setup(fan_relay_channel, GPIO.OUT)
GPIO.setup(sensor_channel, GPIO.IN)

def read_sensor():
    humidity, temperature = DHT.read_retry(DHT.AM2302, sensor_channel)
    return { "humidity": humidity, "temperature": temperature }

def set_fan_state(state):
    GPIO.output(fan_relay_channel, state)

while True:
    readings = read_sensor()
    with open("log", "a") as outfile:
        outfile.write("{0},{1},{2}\n".format(time.time(), readings["humidity"], readings["temperature"]))
    time.sleep(30)

