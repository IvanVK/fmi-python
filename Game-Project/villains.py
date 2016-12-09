from entity import Entity

class Villains(Entity):
    def __init__(self, name, health, berserc):# berserk shte e  chislo(float) mejdu 1 i 2 i shte nanasq syotvetno demage = "demage" + "demage" x "berserk" 
        super().__init__(name, health)
        if berserc < 1:
            self.berserc = 1
        elif berserc > 2:
            self.berserc = 2
        else:
            self.berserc = berserc

    def attack(self):
        if not self.has_weapon():
            return 0
        else:
            if self.weapon.critical_hit():
                return 2 * self.berserc * self.weapon.demage
            else:
                return self.berserc * self.weapon.demage