# coding: utf-8
import os
import requests
import json

class Coffee(object):
    def __init__(self, coffee_type, coffee_size, coffee_number):
        self.__coffee_type = coffee_type
        self.__coffee_size = coffee_size
        self.__coffee_number = coffee_number

    
    def seach_coffee(self):
        params = {"coffee_type":self.__coffee_type, "coffee_size":self.__coffee_size, "coffee_number":self.__coffee_number}
        print(json.dumps(params, ensure_ascii=False))

    def get_coffee_type(self):
        return self.__coffee_type
    
    def get_coffee_size(self):
        return self.__coffee_size
    
    def get_coffee_number(self):
        return self.__coffee_number

def main():
    w = Coffee("拿铁","大杯",'2')
    w.seach_coffee()

if __name__ == '__main__':
    main()