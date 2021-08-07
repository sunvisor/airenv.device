import requests


class Logger:

    def __init__(self, place):
        self.base_url = "http://192.168.0.231/"
        self.place = place
        pass

    def log(self, item_name, item_value):
        url = self.base_url + 'add' + '/' + item_name + '/' + self.place + '/' + str(item_value)
        requests.post(url)


if __name__ == "__main__":
    logger = Logger('test')
    logger.log('co2', 500)
