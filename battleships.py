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


p1_board = sea()

p1_board.add_vessel('C', [3,3], 'S')

p1_board.display()