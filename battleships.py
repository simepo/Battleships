"""Battleships
"""

import random

# Global definitions
vessels = {'C': 5, 'B': 4, 'R': 3, 'S': 3, 'D': 2}
# vessels = {'C': 0, 'B': 0, 'R': 0, 'S': 0, 'D': 2}


# Classes / functions
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

    def display_shots(self):

        print '    0  1  2  3  4  5  6  7  8  9'
        print '  -------------------------------'
        for v in range(10):
            print '%s |' % v,
            for h in range(10):
                if self.water[h][v] in ['C', 'B', 'R', 'S', 'D']:
                    square = ' '
                else:
                    square = self.water[h][v]
                print square + '|',
            print ''
            print '  -------------------------------'

    def add_vessel(self, vessel_type, location, orientation):
        # print 'Adding %s at %s %s' % (vessel_type, location, orientation)
        if orientation == 'E':
            if location[0] + vessels[vessel_type] > 10:
                return False
            for h in range(location[0], location[0] + vessels[vessel_type]):
                if self.water[h][location[1]] != ' ':
                    for reverse_h in range(h - 1, location[0] - 1, -1):
                        self.water[reverse_h][location[1]] = ' '
                    return False
                self.water[h][location[1]] = vessel_type
        elif orientation == 'S':
            if location[1] + vessels[vessel_type] > 10:
                return False
            for v in range(location[1], location[1] + vessels[vessel_type]):
                if self.water[location[0]][v] != ' ':
                    for reverse_v in range(v - 1, location[1] - 1, -1):
                        self.water[location[0]][reverse_v] = ' '
                    return False
                self.water[location[0]][v] = vessel_type
        return True

    def shoot(self, location):
        if self.water[location[0]][location[1]] == ' ':
            self.water[location[0]][location[1]] = 'M'
            return 'Miss'
        elif self.water[location[0]][location[1]] == 'M' or \
                        self.water[location[0]][location[1]] == 'H':
            return 'Repeat'
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


def get_coords():
    print 'Enter co-ordinates, origin top left, 0-9'
    while True:
        try:
            x = int(raw_input('Across: '))
            y = int(raw_input('Down: '))
        except ValueError:
            print 'Please enter an integer'
            continue
        if x < 0 or x > 9 or y < 0 or y > 9:
            print 'Co-ordinates must be between 0 and 9'
            continue
        else:
            break
    return [x, y]


def human_place_ships(board):
    board.display()
    for vessel, size in vessels.iteritems():
        print vessel
        while True:
            location = get_coords()
            while True:
                direction = str(raw_input('Direction (E or S): ')).upper()
                if direction in ['E', 'S']:
                    break
                print 'East or South, try again'
            if board.add_vessel(vessel, location, direction):
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
human_board = sea()
computer_board = sea()

# Place ships
human_board = human_place_ships(human_board)
computer_board = computer_place_ships(computer_board)

# Take shots until somebody wins
while not human_board.lost() and not computer_board.lost():
    computer_board.display_shots()
    location = get_coords()
    print computer_board.shoot(location)
    print human_board.shoot([random.randint(0, 9), random.randint(0, 9)])
    human_board.display()
