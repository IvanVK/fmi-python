from random import randint
from hero import Hero
from villains import Villains


class Fight():
    def __init__(self, hero, villains):
        self.hero = None
        self.villains = None
        self.first = None
        if type(hero) is Hero and type(villains) is Villains:
            self.hero = hero
            self.villains = villains
        else:
            raise ValueError('Wrong type of arguments! Given {}'.format(type(villains)))
        if randint(0, 100) < 50:
            self.first = 1
        else:
            self.first = 2

    def simulate_fight(self):
        fight_result = []
        on_turn = self.first
        while self.hero.is_alive() and self.villains.is_alive():
            if on_turn == 1:
                hero_demage = self.hero.attack()
                self.villains.take_demage(hero_demage)
                fight_result.append('%s hits %s for %d demage!' %\
                        (self.hero.name, self.villains.name, hero_demage))
                on_turn = 2
            else:
                villains_demage = self.villains.attack()
                self.hero.take_demage(villains_demage)
                fight_result.append('%s hits %s for %d demage!' %\
                        (self.villains.name, self.hero.name, villains_demage))
                on_turn = 1
        winner = ''
        if self.hero.is_alive():
            fight_result.append('%s wins the fight!' % (self.hero.name))
            winner = 'Hero'
        else:
            fight_result.append('%s wins the fight!' % (self.villains.name))
            winner = 'Villains'
        return ('\n'.join(fight_result), winner)