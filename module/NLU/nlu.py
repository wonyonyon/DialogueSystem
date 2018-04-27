import copy
import sys
sys.path.append("/Users/tini/NLP/chatbot/DialogueSystem")
from module.NLU.slot_extract.rule_based_extractor import RuleBasedExtrator
from module.NLU.dialog_act_type.rule_based_estimator import Estimator

class RuleBasedNLU(object):
    def __init__(self):
        self.__estimator = Estimator()
        self.__extrator = RuleBasedExtrator()

    def execute(self, sent):
        slot = self.__extrator.extract(sent)
        act_type = self.__estimator.estimator(slot)
        state = {'user_act_type': act_type}
        slot_cp = copy.copy(slot)

        for k,v in slot_cp.items():
            if v =='':
                del slot[k]
        state.update(slot)

        return state

