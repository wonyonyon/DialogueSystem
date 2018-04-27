import re
from knowledge.reader import read_location

class RuleBasedExtrator(object):
    def __init__(self):
        self.__locations = read_location()

    def extract(self, text):
        slot = {'LOCATION': self.__extract_locations(text)}

        return slot

    def __extract_locations(self, text):
        locations = [loc for loc in self.__locations if loc in text]
        locations.sort(key=len, reverse=True)
        location = locations[0] if len(locations) > 0 else ''
        print(locations)
        return location

    def __extract_number(self, text):
        pass
