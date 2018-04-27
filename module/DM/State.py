#coding: utf-8
import sys
sys.path.append("/Users/tini/NLP/chatbot/DialogueSystem")
'''
function:
    dialog state manage()
    select data from knowlebase 
'''

class State(object):
    def __init__(self):
        self.__state = {"location":None}

    def update(self,dialog_act):
        self.__state["location"] = dialog_act.get('location', self.__state['location'])

    
    def has(self, name):
        return self.__state.get(name,None) != None
    # state map many get function
    def get_location(self):
        return self.__state['location']
    
    def get_state_name(self):
        pass

    def clear(self):
        self.__init__()

    def __str__(self):
        import pprint
        return pprint.pformat(self.__state)