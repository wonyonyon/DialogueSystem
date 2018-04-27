import sys
sys.path.append("/Users/tini/NLP/chatbot/DialogueSystem")
from copy import deepcopy
from module.DM.State import State
from module.Service.weather import Weather

class Manager(object):
    def __init__(self):
        self.state = State()

    def update_state(self, dialog_act):
        self.state.update(dialog_act)

    def select_action(self, dialog_act):
        system_act = deepcopy(dialog_act)
        if dialog_act['user_act_type'] == "OTHER":
            print("调用闲聊模块")
        elif not self.state.has("location"):
            system_act['sys_act_type'] = 'REQUEST_LOCATION'
        else:
            location = self.state.get_location()
            api = Weather(location)
            weather = api.search_weather()
            system_act['sys_act_type'] = 'INFORM_WEATHER'
            system_act['weather'] = weather
            self.state.clear()

        return system_act
