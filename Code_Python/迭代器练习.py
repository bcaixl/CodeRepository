# -*- coding:utf-8 -*-
# Using python 2.7
import requests
from collections import Iterable, Iterator


class WeatherIterator(Iterator):
    def __init__(self, citices):
        self.citices = citices
        self.index = 0

    def get_weather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city='+city)
        data = r.json()['data']['forecast'][0]
        return '%s:%s,%s' % (city, data['low'], data['high'])

    def next(self):
        if self.index == len(self.citices):
            raise StopIteration
        city = self.citices[self.index]
        self.index += 1
        return self.get_weather(city)


class WeatherIterable(Iterable):
    def __init__(self, citices):
        self.cities = citices

    def __iter__(self):
        return WeatherIterator(self.cities)


if __name__ == '__main__':
    for x in WeatherIterable([u'北京', u'上海', u'广州', u'深圳']):
        print x.encode('utf-8')
