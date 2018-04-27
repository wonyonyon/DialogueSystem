# coding: utf-8

class Estimator(object):
    def __init__(self):
        pass

    def estimator(self,slot):
        if slot["LOCATION"] != '':
            return 'INFORM_LOCATION'
        else:
            return 'OTHER'