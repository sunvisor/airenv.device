import RPi.GPIO as GPIO
from threading import Timer


class Led:
    def __init__(self):
        self.port = 0
        self.color_map = {
            'red': 17,
            'yellow': 27,
            'green': 22,
        }
        self._blink_status = GPIO.LOW
        self._blink_timer = None
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        self.clear()

    def select(self, color):
        self.blink_stop()
        port = self.color_map.get(color, 0)
        self.led_on(port)

    def led_on(self, port):
        if port == 0:
            self.clear()
            return
        if self.port == port:
            return
        if self.port != 0:
            GPIO.output(self.port, GPIO.LOW)
        GPIO.output(port, GPIO.HIGH)
        self.port = port

    def blink_start(self, color, interval):
        def handler(color, interval):
            port = self.color_map.get(color, 0)
            self.toggle_blink_status()
            GPIO.output(port, self._blink_status)
            self.blink_start(color, interval)

        self._blink_timer = Timer(interval, handler, (color, interval, ))
        self._blink_timer.start()

    def blink_stop(self):
        if self._blink_timer is None:
            return
        self._blink_timer.cancel()
        self._blink_timer = None
        self.clear()

    def toggle_blink_status(self):
        if self._blink_status == GPIO.LOW:
            self._blink_status = GPIO.HIGH
        else:
            self._blink_status = GPIO.LOW

    def clear(self):
        GPIO.output(17, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
