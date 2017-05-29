import Adafruit_DHT as DHT
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

fan_relay_channel = 13
sensor_channel = 11

GPIO.setup(fan_relay_channel, GPIO.OUT)
GPIO.setup(sensor_channel, GPIO.IN)

def read_sensor():
    humidity, temperature = DHT.read_retry(DHT.AM2302, sensor_channel)
    return { "humidity": humidity, "temperature": temperature }

def set_fan_state(state):
    GPIO.output(fan_relay_channel, state)

print read_sensor()
