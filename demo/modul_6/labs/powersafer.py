from baseclass import BaseClass

class PowerSafer(BaseClass):
    def __init__(self, is_on, liquid, temp, alert_state, temp_deviation, leistung, vereisung):
        super().__init__(is_on, liquid, temp, alert_state, temp_deviation)
        self.__leistung = leistung
        self.__vereisung = vereisung

    def get_leistung(self):
        return self.__leistung

    def get_vereisung(self):
        return self.__vereisung        