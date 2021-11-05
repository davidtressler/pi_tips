import RPi.GPIO as GPIO #
import time 

GPIO.setwarnings(False) #NOTE: raspberry pi could be updated, and you might need to change your code
GPIO.setmode(GPIO.BCM) 
GPIO.setup(14, GPIO.OUT)


while True:
      GPIO.output(14, True) 
      time.sleep(1) 
      GPIO.output(14, False) 
      time.sleep(1) 
