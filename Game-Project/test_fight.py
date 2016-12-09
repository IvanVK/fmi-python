import unittest
import fight
from hero import Hero
from villains import Villains
from weapon import Weapon


class FightTest(unittest.TestCase):
    def setUp(self):
        weapon = Weapon('Dagger', 10, 0.0)
        hero = Hero('our hero', 100, 'Hero1')
        hero.equip_weapon(weapon)
        villains = Villains('Vill', 1, 1.4)
        villains.equip_weapon(weapon)
        self.fight = fight.Fight(hero, villains)

    def test_initialize_fight(self):
        self.assertNotEqual(None, self.fight.hero)
        self.assertNotEqual(None, self.fight.villains)
        self.assertIn(self.fight.first, [1, 2])

    def test_simulate_fight(self):
        hero_starts = 'our hero hits Vill for 10 demage!\n' \
                            'our hero wins the fight!'
        villains_starts = 'Vill hits our hero for 14 demage!\n' \
                            'our hero hits Vill for 10 demage!\n' \
                            'our hero wins the fight!'
        if self.fight.first is 1:
            self.assertEqual(hero_starts, self.fight.simulate_fight()[0])
        else:
            self.assertEqual(villains_starts, self.fight.simulate_fight()[0])

if __name__ == '__main__':
    unittest.main()