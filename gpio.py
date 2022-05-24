import RPi.GPIO as GPIO

def light_LED():
    LED_PIN = 14
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.HIGH)
    GPIO.cleanup()
