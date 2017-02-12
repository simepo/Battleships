"""Battleships
"""

import random

# Global definitions
vessels = {'C': 5, 'B': 4, 'R': 3, 'S': 3, 'D': 2}
#vessels = {'C': 0, 'B': 0, 'R': 0, 'S': 0, 'D': 2}

#Classes / functions
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

        self.vessels = vessels

    def display(self):

        print '    0  1  2  3  4  5  6  7  8  9'
        print '  -------------------------------'
        for v in range(10):
            print '%s |' % v,
            for h in range(10):
                print self.water[h][v] + '|',
            print ''
            print '  -------------------------------'

    def add_vessel(self, vessel_type, location, orientation):
        if orientation == 'E':
            if location[0] + vessels[vessel_type] > 10:
                return False
            for h in range(location[0], location[0] + vessels[vessel_type]):
                if self.water[h][location[1]] != ' ':
                    return False
                self.water[h][location[1]] = vessel_type
        elif orientation == 'S':
            if location[1] + vessels[vessel_type] > 10:
                return False
            for v in range(location[1], location[1] + vessels[vessel_type]):
                if self.water[location[0]][v] != ' ':
                    return False
                self.water[location[0]][v] = vessel_type
        return True

    def shoot(self, location):
        if self.water[location[0]][location[1]] == ' ' or self.water[location[0]][location[1]] == 'M':
            self.water[location[0]][location[1]] = 'M'
            return 'Miss'
        else:
            vessel_type = self.water[location[0]][location[1]]
            self.water[location[0]][location[1]] = 'H'
            self.vessels[vessel_type] -= 1
            if self.vessels[vessel_type] == 0:
                return 'Sunk ' + vessel_type
            else:
                return 'Hit'

    def lost(self):
        vessels_remaining = 0
        for vessel, remaining in self.vessels.iteritems():
            vessels_remaining += remaining
        if vessels_remaining == 0:
            return True
        else:
            return False


def human_place_ships(board):
    board.display()
    for vessel, size in vessels.iteritems():
        print vessel
        while True:
            print 'Enter co-ordinates, origin top left, 0-9'
            x = int(raw_input('Across: '))
            y = int(raw_input('Down: '))
            while True:
                direction = str(raw_input('Direction (E or S): ')).upper()
                if direction in ['E', 'S']:
                    break
                print 'East or South, try again'
            if board.add_vessel(vessel, [x, y], direction):
                break
            print 'Invalid entry, try again'
            print ''
        board.display()
        print ''
    return board


def computer_place_ships(board):
    for vessel, size in vessels.iteritems():
        while True:
            if random.randint(0, 1) == 0:
                direction = 'E'
            else:
                direction = 'S'
            if direction == 'E':
                x = random.randint(0, 9 - size)
                y = random.randint(0, 9)
            else:
                x = random.randint(0, 9)
                y = random.randint(0, 9 - size)
            if board.add_vessel(vessel, [x, y], direction):
                break
    return board

# Main program loop
# Initiate boards
#p1_board = sea()
p2_board = sea()

# Place ships
#p1_board = human_place_ships(p1_board)
p2_board = computer_place_ships(p2_board)

# Take shots until somebody wins


"""
p1_board.add_vessel('D', [3,3], 'S')

print p1_board.shoot([3, 3])
print p1_board.lost()
p1_board.display()
print p1_board.shoot([3, 4])
print p1_board.lost()
"""
p2_board.display()