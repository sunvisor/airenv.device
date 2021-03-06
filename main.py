from time import sleep
from ccs811 import Co2Sensor
from led import Led
from judge import co2_judge
from logger import Logger
from switch import Switch

sensor = Co2Sensor()
led = Led()
logger = Logger('home_office')
switch = Switch(led, sensor)

count = 0
try:
    while True:
        sleep(1)
        value = sensor.read_data()
        co2 = value['co2']
        count = count + 1
        if not sensor.is_reliable():
            led.blink_start('green', 1)
            continue
        if co2 > 400 and count >= 60:
            led.select(co2_judge(co2))
            logger.log('co2', co2)
            count = 0
except KeyboardInterrupt:
    led.clear()
