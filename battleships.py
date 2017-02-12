"""Battleships
"""

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

        print '-------------------------------'
        for v in range(10):
            print '|',
            for h in range(10):
                print self.water[h][v] + '|',
            print ''
            print '-------------------------------'

    def add_vessel(self, vessel_type, location, orientation):
        if orientation == 'E':
            for h in range(location[0], location[0] + vessels[vessel_type]):
                self.water[h][location[1]] = vessel_type
        elif orientation == 'S':
            for v in range(location[1], location[1] + vessels[vessel_type]):
                self.water[location[0]][v] = vessel_type

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
        print 'Enter co-ordinates, origin top left, 0-9'
        x = int(raw_input('Across: '))
        y = int(raw_input('Down: '))
        direction = str(raw_input('Direction (E or S): '))
        print vessel, [x, y], direction
        board.add_vessel(vessel, [x, y], direction)
        board.display()
        print ''
    return board

# Main program loop
# Initiate boards
p1_board = sea()
#p2_board = sea()

# Place ships
p1_board = human_place_ships(p1_board)
#p2_board = computer_place_ships(p2_board)

# Take shots until somebody wins


"""
p1_board.add_vessel('D', [3,3], 'S')

print p1_board.shoot([3, 3])
print p1_board.lost()
p1_board.display()
print p1_board.shoot([3, 4])
print p1_board.lost()
"""
p1_board.display()