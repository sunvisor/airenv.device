from time import sleep
from ccs811 import Co2Sensor
from led import Led
from judge import co2_judge
from logger import Logger

sensor = Co2Sensor()
led = Led()
logger = Logger('home_office')
count = 0
while True:
    value = sensor.read_data()
    led.select(co2_judge(value['co2']))
    count = count + 1
    if count > 20:
        logger.log('co2', value['co2'])
        count = 0;
    sleep(3)
