import sys
from copy import deepcopy
from module.DM.State import State
from module.Service.api_coffee import Coffee

class Manager(object):
    def __init__(self):
        self.state = State()

    def update_state(self, dialog_act):
        self.state.update(dialog_act)

    def select_action(self, dialog_act):
        system_act = deepcopy(dialog_act)
        if not self.state.has('TYPE'):
            system_act['sys_act_type'] = 'REQUEST_TYPE'
        elif not self.state.has("SIZE"):
            system_act['sys_act_type'] = 'REQUEST_SIZE'
        elif not self.state.has("NUMBER"):
            system_act['sys_act_type'] = 'REQUEST_NUMBER'
        else:
            coffee_type = self.state.get_type()
            coffee_size = self.state.get_size()
            coffee_number = self.state.get_number()
            coffee_size = self.state.get_size()

            coffee = Coffee(coffee_type, coffee_size, coffee_number)
            # search_coffee = coffee.seach_coffee()
            system_act['sys_act_type'] = 'INFORM_COFFEE'
            system_act['coffee'] = coffee
            self.state.clear()

        return system_act
