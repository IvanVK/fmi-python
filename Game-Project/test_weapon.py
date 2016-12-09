import unittest
import weapon


class WeaponTest(unittest.TestCase):

    def setUp(self):
        self.test_weapon = weapon.Weapon('Dagger', 20, 0.2)

    def test_initialize_weapon(self):
        self.assertEqual('Dagger', self.test_weapon.type)
        self.assertEqual(20, self.test_weapon.demage)
        self.assertEqual(0.2, self.test_weapon.critical_strike_percent)

    def test_critical_hit(self):
        t_count = 0
        f_count = 0
        for _ in range(1000):
            if self.test_weapon.critical_hit():
                t_count += 1
            else:
                f_count += 1
        allowance = range(100, 300)
        hit_percent = int((t_count / f_count) * 1000)
        self.assertIn(hit_percent, allowance)

if __name__ == '__main__':
    unittest.main()