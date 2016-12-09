import unittest
import villains
import weapon

class VillainsTest(unittest.TestCase):

    def setUp(self):
        self.villains = villains.Villains('vill', 100, 1.5)

    def test_initialize_villains(self):
        self.assertEqual('vill', self.villains.name)
        self.assertEqual(100, self.villains.health)
        self.assertEqual(1.5, self.villains.berserc)

    def test_attack(self):
        weap = weapon.Weapon('dagger', 30, 0.2)
        self.villains.equip_weapon(weap)
        possible_demage = [45, 90]
        self.assertIn(self.villains.attack(), possible_demage)

if __name__ == '__main__':
    unittest.main()