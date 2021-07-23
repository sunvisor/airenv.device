import board
import adafruit_ccs811


class Co2Sensor:

    def __init__(self):
        board.SCL, board.SDA
        i2c = board.I2C()  # uses board.SCL and board.SDA
        self.ccs811 = adafruit_ccs811.CCS811(i2c)
        pass

    def read_data(self):
        while not self.ccs811.data_ready:
            pass
        try:
            result = {
                'co2': self.ccs811.eco2,
                'tvoc': self.ccs811.tvoc,
            }
        except OSError as e:
            return {
                'co2': -1,
                'tvoc': -1,
            }
        return result
