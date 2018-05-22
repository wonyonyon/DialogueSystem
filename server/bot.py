import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from module.DM.manage import Manager
from module.NLG.generator import NLGenerator
from module.NLU.nlu import RuleBasedNLU

class Bot(object):
    def __init__(self):
        self.generator = NLGenerator()
        self.nlu = RuleBasedNLU()
        self.manager = Manager()

    def reply(self, sent):
        dialog_act = self.nlu.execute(sent)

        self.manager.update_state(dialog_act)
        system_act_type = self.manager.select_action(dialog_act)

        sent = self.generator.generate_sentence(system_act_type)

        return sent

def main():
    bot = Bot()
    # generator = NLGenerator()
    # nlu = RuleBasedNLU()
    # manager = Manager()
    print("S:你好，请问有什么可以为您服务的吗？")
    while True:
        sent = input("U: ")
        if sent == "谢谢":
            print('S: 不客气')
            break
        sent = bot.reply(sent)
        print(sent)


if __name__ == '__main__':
    main()