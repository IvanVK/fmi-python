from random import randint

class Weapon():
    def __init__(self, type, demage, critical_strike_percent):
        self.type = type
        self.demage = demage
        if critical_strike_percent < 0:
            self.critical_strike_percent = 0
        elif critical_strike_percent > 1:
            self.critical_strike_percent = 1
        else:
            self.critical_strike_percent = critical_strike_percent

    def critical_hit(self):
        if randint(0, 100) < self.critical_strike_percent * 100:
            return True
        return False