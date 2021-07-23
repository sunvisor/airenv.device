import RPi.GPIO as GPIO


class Led:
    def __init__(self):
        self.port = 0
        self.color_map = {
            'red': 17,
            'yellow': 27,
            'green': 22,
        }
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        self.clear()

    def select(self, color):
        port = self.color_map.get(color, 0)
        self.led_on(port)

    def led_on(self, port):
        if port == 0:
            self.clear()
            return
        if self.port == port:
            return
        GPIO.output(self.port, GPIO.LOW)
        GPIO.output(port, GPIO.HIGH)
        self.port = port

    @staticmethod
    def clear():
        GPIO.output(17, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
