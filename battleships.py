"""Battleships
"""


class sea:

    def __init__(self):

        self.water = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

        self.vessel = {'C': 5, 'B': 4, 'R': 3, 'S': 3, 'D': 2}

    def display(self):

        print '-------------------------------'
        for v in range(10):
            print '|',
            for h in range(10):
                print self.water[h][v] + '|',
            print ''
            print '-------------------------------'

    def add_vessel(self, type, location, orientation):

        if type is 'C':
            vessel_length = 5
        elif type is 'B':
            vessel_length = 4
        elif type is 'R':
            vessel_length = 3
        elif type is 'S':
            vessel_length = 3
        elif type is 'D':
            vessel_length = 2

        if orientation is 'E':
            for h in range(location[0], location[0] + vessel_length):
                self.water[h][location[1]] = type
        elif orientation is 'S':
            for v in range(location[1], location[1] + vessel_length):
                self.water[location[0]][v] = type

    def shoot(self, location):
        if self.water[location[0]][location[1]] == ' ' or self.water[location[0]][location[1]] == 'M':
            self.water[location[0]][location[1]] = 'M'
            return 'Miss'
        else:
            vessel_type = self.water[location[0]][location[1]]
            self.water[location[0]][location[1]] = 'H'
            self.vessel[vessel_type] -= 1
            if self.vessel[vessel_type] == 0:
                return 'Sunk ' + vessel_type
            else:
                return 'Hit'

p1_board = sea()

p1_board.add_vessel('D', [3,3], 'S')

print p1_board.shoot([3, 3])
print p1_board.shoot([3, 4])

p1_board.display()