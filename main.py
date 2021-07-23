from time import sleep
from ccs811 import Co2Sensor
from led import Led
from judge import co2_judge


sensor = Co2Sensor()
led = Led()
while True:
    value = sensor.read_data()
    led.select(co2_judge(value.co2))
    sleep(30)
