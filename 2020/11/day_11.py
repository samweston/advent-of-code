
# . = floor
# L = empty
# # = occupied.

# If seat is empty, and no adjacent occupied seats
#   => becomes occupied
# If seat is occupied and four or more seats adjacent are occupied
#   => becomes empty

FLOOR, EMPTY, OCCUPIED = 0, 1, 2
STATE_CHARS = [ '.', 'L', '#' ]

def print_board(board):
    max_x = max([ position[0] for position in board.keys() ])
    max_y = max([ position[1] for position in board.keys() ])

    for x in range(0, max_x + 1):
        line = ''
        for y in range(0, max_y + 1):
            line += STATE_CHARS[board[(x, y)]]
        print(line)

def adjacent_occupied_1(position, board):
    count = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            adjacent_position = (position[0] + i, position[1] + j)
            if adjacent_position != position and \
                    adjacent_position in board and \
                    board[adjacent_position] == OCCUPIED:
                count += 1
    return count

def step_1(board):
    new_board = dict()
    for position, state in board.items():
        new_state = state
        if state == EMPTY and adjacent_occupied_1(position, board) == 0:
            new_state = OCCUPIED
        elif state == OCCUPIED and adjacent_occupied_1(position, board) >= 4:
            new_state = EMPTY
        new_board[position] = new_state
    return new_board

def calc_position(i, j, m, position):
    return (i * m + position[0], j * m + position[1])

def adjacent_occupied_2(position, board):
    count = 0
    
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if not (i == 0 and j == 0):
                m = 1
                while calc_position(i, j, m, position) in board:
                    state = board[calc_position(i, j, m, position)]
                    if state == OCCUPIED:
                        count += 1
                        break
                    elif state == EMPTY:
                        break
                        
                    m += 1
    
    return count

def step_2(board):
    new_board = dict()
    for position, state in board.items():
        new_state = state
        if state == EMPTY and adjacent_occupied_2(position, board) == 0:
            new_state = OCCUPIED
        elif state == OCCUPIED and adjacent_occupied_2(position, board) >= 5:
            new_state = EMPTY
        new_board[position] = new_state
    return new_board

def read_board():
    board = dict()
    with open('2020/11/input', 'r') as f:
        lines = [ line.strip() for line in f.readlines() ]
        for i, line in enumerate(lines):
            for j, state_char in enumerate(line):
                board[(i, j)] = STATE_CHARS.index(state_char)
    return board

def part_1():
    board = read_board()
    
    steps = 1
    while True:
        new_board = step_1(board)
        
        if new_board == board:
            return len(list(filter(lambda v: v == OCCUPIED, new_board.values())))
            
        steps += 1
        board = new_board

def part_2():
    board = read_board()

    steps = 1
    while True:
        new_board = step_2(board)
        
        if new_board == board:
            return len(list(filter(lambda v: v == OCCUPIED, new_board.values())))
            
        steps += 1
        board = new_board

if __name__ == '__main__':
    print('2020 day 11')
    print(f'part_1={part_1()}')
    print(f'part_2={part_2()}')
