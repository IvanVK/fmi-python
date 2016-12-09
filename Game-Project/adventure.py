from hero import Hero
from villains import Villains
from fight import Fight


class Adventure():
    def __init__(self, map_path):
        map_file = open(map_path, 'r')
        self.map = map_file.read().splitlines()
        map_file.close()
        self.map = [list(x) for x in self.map]
        self.players = {}

    def print_map(self):
        printing_map = '\n'.join([''.join(x) for x in self.map])
        print(printing_map)
        return printing_map

    def spawn(self, name, entity):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 'P':
                    if type(entity) is Hero:
                        self.map[i][j] = 'H'
                        self.players[name] = [entity, (i, j)]
                        return True
                    elif type(entity) is Villains:
                        self.map[i][j] = 'V'
                        self.players[name] = [entity, (i, j)]
                        return True
                    else:
                        break
        return False

    def move(self, player, direction):
        if player in self.players:
            position = self.players[player][1]
            new_position = ()

            oponent = 'V' if type(self.players[player][0]) is Hero else 'H'

            if direction == 'right' and position[1] + 1 < len(self.map[position[0]]):
                new_position = (position[0], position[1] + 1)

            elif direction == 'left' and position[1] - 1 >= 0:
                new_position = (position[0], position[1] - 1)

            elif direction == 'up' and position[0] - 1 >= 0:
                new_position = (position[0] - 1, position[1])

            elif direction == 'down' and position[0] + 1 < len(self.map):
                new_position = (position[0] + 1, position[1])

            else:
                return False

            if self.map[new_position[0]][new_position[1]] == '.':
                self.map[new_position[0]][new_position[1]] = self.map[position[0]][position[1]]
                self.map[position[0]][position[1]] = '.'
                self.players[player][1] = new_position
                return True

            elif self.map[new_position[0]][new_position[1]] == oponent:
                for oponent_name in self.players:

                    if self.players[oponent_name][1] == new_position:
                        fight = Fight(self.players[player][0], self.players[oponent_name][0])

                        if not fight is None:
                            fight_outcome = fight.simulate_fight()
                            print(fight_outcome[0])

                            if fight_outcome[1] == 'H':
                                self.players.pop(oponent_name)
                                self.players[player][1] = new_position
                                self.map[new_position[0]][new_position[1]] = self.map[position[0]][position[1]]
                                self.map[position[0]][position[1]] = '.'

                            elif fight_outcome[1] == 'V':
                                self.players.pop(player)
                                self.map[position[0]][position[1]] = '.'

                            return fight_outcome[1]
            else:
                return False