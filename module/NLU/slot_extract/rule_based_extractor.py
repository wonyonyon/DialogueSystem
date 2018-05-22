import re
from knowledge.reader import read_location

class RuleBasedExtrator(object):
    def __init__(self):
        self.__coffee_type = ['拿铁','美式','摩卡'] #可以添加yaml配置文件添加类型
        self.__coffee_size = ['大杯','小杯']
        self.__coffee_number = ['1','2','3', '4']

    def extract(self, text):
        slot = {'TYPE': self.__extract_type(text), 'SIZE':self.__extract_size(text), 'NUMBER': self.__extract_number(text)}

        return slot

    def __extract_type(self, text):
        coffee_type = [c_type for c_type in self.__coffee_type if c_type in text]
        coffee_type.sort(key=len, reverse=True)
        c_type = coffee_type[0] if len(coffee_type) > 0 else ''
        # print(locations)
        return c_type

    def __extract_size(self, text):
        coffee_size = [size for size in self.__coffee_size if size in text]
        coffee_size.sort(key=len, reverse=True)
        size = coffee_size[0] if len(coffee_size) > 0 else ''
        # print(locations)
        return size

    def __extract_number(self, text):
        #考虑数字（1，2，3，4）和汉字（一二三四）
        pattern = re.compile('\d+|[一二三四五六七]')
        # pattern = re.compile('[一二三四五六七{1,}]')
        res = re.findall(pattern, text)
        if len(res) == 1:
            return ''.join(res)
        else:  
            return ''
