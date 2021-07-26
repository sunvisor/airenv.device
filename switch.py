import RPi.GPIO as GPIO

SWITCH_PORT = 23


class Switch:
    def __init__(self, led, sensor):
        self.led = led
        self.sensor = sensor
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SWITCH_PORT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(SWITCH_PORT, GPIO.RISING, callback=self.on_reset, bouncetime=200)

    def on_reset(self, channel):
        if channel == SWITCH_PORT:
            print('reset', channel)
            self.led.clear()
            self.sensor.init()
