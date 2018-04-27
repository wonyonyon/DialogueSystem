import sys

sys.path.append("/Users/tini/NLP/chatbot/DialogueSystem")
class NLGenerator(object):
    def __init__(self):
        pass

    def generate_sentence(self, dialog_act):
        sent = ""
        
        system_act_type = dialog_act['sys_act_type']
        if system_act_type  == "REQUEST_LOCATION":
            sent += "请输入你要查询的城市"
        elif system_act_type == "CHAT":
            print("闲聊")
        elif system_act_type == "INFORM_WEATHER":
            # if "LOCATION" in dialog_act:
            # sent += '你要问的城市为{0}'.format(dialog_act['LOCATION'])
            weather = dialog_act['weather']
            if weather:
                sent += "{0}的pm25为{1}，空气质量{2}，{3}".format(dialog_act['LOCATION'],weather['pm25'],weather['quality'],weather['ganmao'])
            else:
                sent += "对不起，没有找到你要查询的城市。"

        else:
            print("ERROR")
            sys.exit(1)
        
        return sent