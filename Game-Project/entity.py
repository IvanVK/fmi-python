import weapon


class Entity():
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = None

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health > 0

    def take_healing(self, healing_points):
        if self.is_alive():
            self.health += healing_points
        else:
            return False
        if self.health > self.max_health:
            self.health = self.max_health

    def take_demage(self, demage):
        if self.is_alive():
            self.health -= demage
        if self.health < 0:
            self.health = 0

    def has_weapon(self):
        return not self.weapon is None

    def equip_weapon(self, new_weapon):
        if type(new_weapon) is weapon.Weapon:
            self.weapon = new_weapon

    def attack(self):
        if not self.has_weapon():
            return 0
        else:
            if self.weapon.critical_hit():
                return 2 * self.weapon.demage
            else:
                return self.weapon.demage