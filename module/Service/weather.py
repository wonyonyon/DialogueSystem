import os
import requests

class Weather(object):
    BASE_URL = "https://www.sojson.com/open/api/weather/json.shtml"

    def __init__(self, city):
        self.__city = city

    # def __search(self, **kwargs):
    #     params = {"city":self.__city}
    #     params.update(kwargs)
    #     response = requests.get(self.BASE_URL,params=params)

    #     return response

    def search_weather(self):
        params = {"city":self.__city}
        # params.update(kwargs)
        response = requests.get(self.BASE_URL,params=params)
        result = response.json()

        return result['data']


def main():
    w = Weather("深圳")
    w.search_weather()

if __name__ == '__main__':
    main()