import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
for i in range(6):
    print("Light on")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    print("Light off")
    GPIO.output(18,GPIO.LOW)
    time.sleep(1)