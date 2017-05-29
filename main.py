import Adafruit_DHT as DHT
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(fan_relay_channel, GPIO.OUT)
GPIO.setup(sensor_channel, GPIO.IN)

def read_sensor():
    humidity, temperature = DHT.read_retry(DHT.AM2302, 11)
    return { "humidity": humidity, "temperature": temperature }

def set_fan_state(state):
    GPIO.output(13, state)

print read_sensor
