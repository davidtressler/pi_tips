import RPi.GPIO as GPIO
import dht11

    # initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


    # read data using pin 19
instance = dht11.DHT11(pin = 14)
result = instance.read()

if result.is_valid():
    print("Temperature: %-3.1f C" % result.temperature)
    print("Humidity: %-3.1f %%" % result.humidity)
else:
  print("Error")
