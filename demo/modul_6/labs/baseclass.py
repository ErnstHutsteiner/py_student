class BaseClass:
    """
    Basisklasse für Kühlgeräte
    """
    value_preset = {
        "HighTempLimit" : 8,
        "LowTempLimit"  : -84,
        "LowLiquid" : 0,
        "HighLiquid" : 100 
    }
    alert_preset = ["gruen", "gelb", "rot"]
    def __init__(self, is_on, liquid, temp, alert_state, temp_deviation):
       self.__is_on = is_on
       self.__liquid = liquid
       self.__temp = temp
       self.__alert_state = alert_state
       self.__temp_deviation = temp_deviation
       
    def get_is_on(self):
        return self.__is_on

    def get_liquid(self):
        return self.__liquid

    def get_temp(self):
        return self.__temp

    def get_alert_state(self):
        return self.__alert_state

    def get_temp_deviation(self):
        return self.__temp_deviation

    def set_is_on(self, is_on):
        actual_state = self.get_is_on()
        if is_on == True or is_on == False:
            self.__is_on = is_on
        else:
            return (print("ungülitge Eingabe. der Betriebszustand bleibt:" + actual_state))    

    def set_temp(self, temp):
        if self.value_preset["LowTempLimit"] <= temp <= self.value_preset["HighTempLimit"]:
            self.__temp = temp
        else:
            print("value outside of range")    

    def set_liquid(self, liquid_in_percent):
        if self.value_preset["LowLiquid"] <= liquid_in_percent <= self.value_preset["HighLiquid"]:
            self.__liquid = liquid_in_percent
            self.__liquid_alert()
        else:
            print("invalid value for liquid provided")    

    def __set_alert(self, alert):
        if alert in self.alert_preset:
            self.__alert_state = alert
        else:
            print("Alert value does not exist")    

    def __liquid_alert(self):
        if self.__liquid > 80:
            self.__set_alert("gruen")
        elif 80 >= self.__liquid > 60:
            self.__set_alert("gelb")
        else:
            self.__set_alert("rot")
    
    def __temp_deviation_alert(self):
        if (self.__temp - self.__temp_deviation) < self.__temp < (self._temp + self.__temp_deviation):
            self.__set_alert("rot")

