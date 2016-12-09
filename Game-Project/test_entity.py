import unittest
import entity
import weapon


class EntityTest(unittest.TestCase):

    def setUp(self):
        self.test_entity = entity.Entity('Entity', 100)

    def test_initialize_entity(self):
        self.assertEqual('Entity', self.test_entity.name)
        self.assertEqual(100, self.test_entity.health)

    def test_get_health(self):
        self.assertEqual(100, self.test_entity.get_health())

    def test_is_alive(self):
        self.assertTrue(self.test_entity.is_alive())

    def test_is_dead(self):
        self.test_entity.take_demage(130)
        self.assertEqual(False, self.test_entity.is_alive())

    def test_take_demage(self):
        self.test_entity.take_demage(50)
        self.assertEqual(50, self.test_entity.get_health())

    def test_take_killing(self):
        self.test_entity.take_demage(130)
        self.assertEqual(0, self.test_entity.get_health())

    def test_take_healing(self):
        self.test_entity.take_demage(50)
        self.test_entity.take_healing(30)
        self.assertEqual(80, self.test_entity.get_health())

    def test_heal_after_max(self):
        self.test_entity.take_healing(100)
        self.assertEqual(100, self.test_entity.get_health())

    def test_has_no_weapon(self):
        self.assertEqual(False, self.test_entity.has_weapon())

    def test_equip_weapon(self):
        w = weapon.Weapon('dagger', 30, 0.3)
        self.test_entity.equip_weapon(w)
        self.assertTrue(self.test_entity.has_weapon())

    def test_attack(self):
        w = weapon.Weapon('dagger', 30, 0.3)
        self.test_entity.equip_weapon(w)
        possible_demage = [30, 60]
        self.assertIn(self.test_entity.attack(), possible_demage)

if __name__ == '__main__':
    unittest.main()