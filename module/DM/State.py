#coding: utf-8
import sys

'''
function:
    dialog state manage()
    select data from knowlebase 
'''
# based class, can generate different state about hamburger, chips, coke
class State(object):
    def __init__(self):
        self.__state = {"TYPE":None,"SIZE":None, "NUMBER":None}

    def update(self,dialog_act):
        self.__state["TYPE"] = dialog_act.get('TYPE', self.__state['TYPE'])
        self.__state["SIZE"] = dialog_act.get('SIZE', self.__state['SIZE'])
        self.__state["NUMBER"] = dialog_act.get('NUMBER', self.__state['NUMBER'])
    
    def has(self, name):
        return self.__state.get(name) != None
    # state map many get function
    def get_type(self):
        return self.__state['TYPE']
    
    def get_size(self):
        return self.__state['SIZE']
    
    def get_number(self):
        return self.__state['NUMBER']

    def clear(self):
        self.__init__()

    def __str__(self):
        import pprint
        return pprint.pformat(self.__state)