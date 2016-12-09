import unittest
from adventure import Adventure 
from hero import Hero
from villains import Villains
from weapon import Weapon


class AdventureTest(unittest.TestCase):

    def setUp(self):
        self.test_m = ['..##......',
                    '#.##..###.',
                    '#.###.###.',
                    '#..P.P###.',
                    '###.#####.']
        test_map_file = open('test_map.txt', 'w')
        test_map_file.write('\n'.join(self.test_m))
        test_map_file.close()
        self.test_map = Adventure('test_map.txt')

    def test_print_map(self):
        self.assertEqual('\n'.join(self.test_m), self.test_map.print_map())

    def test_spawn(self):
        hero = Hero('player1', 100, 'first')
        villains = Villains('player2', 100, 2)
        self.test_map.spawn('player1', hero)
        self.assertEqual('H', self.test_map.print_map()[36])
        self.assertEqual('P', self.test_map.print_map()[38])
        self.test_map.spawn('player2', villains)
        self.assertEqual('V', self.test_map.print_map()[38])

    def test_move(self):
        after_move = ['..##......',
                    '#.##..###.',
                    '#.###.###.',
                    '#...HV###.',
                    '###.#####.']
        hero = Hero('player1', 100, 'first')
        villains = Villains('player2', 100, 2)
        hero_weapon = Weapon('Axe', 25, 0.1)
        hero.equip_weapon(hero_weapon)
        villains_weapon = Weapon('Stick', 5, 0.01)
        villains.equip_weapon(villains_weapon)
        self.test_map.spawn('player1', hero)
        self.test_map.spawn('player2', villains)
        self.assertTrue(self.test_map.move('player1', 'right'))
        self.assertEqual('\n'.join(after_move), self.test_map.print_map())
        self.test_map.move('player1', 'right')

    def test_fight(self):
        pass

if __name__ == '__main__':
    unittest.main()