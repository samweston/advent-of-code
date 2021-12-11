
# 100 octopuses, in 10 by 10 grid.
# Gain energy, and flash when full.
# Each has an energy level. Between 0 and 9.

def find_neighbours(x, y, array):
    neighbours = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            neighbour_x = x + i
            neighbour_y = y + j
            if neighbour_x >= 0 and neighbour_x < len(array) and \
                    neighbour_y >= 0 and neighbour_y < len(array[0]):
                neighbours.append((neighbour_x, neighbour_y))
    
    return neighbours

def solve():
    with open('2021/11/input', 'r') as f:
        octopuses = [ [ int(c) for c in line.strip() ] for line in f.readlines() ]

    # Count number of flashes after 100 steps.
    flash_count = 0
    iteration = 1
    while True:
        flashed_positions = set()
        # Increment by 1
        for i, line in enumerate(octopuses):
            for j, value in enumerate(line):
                octopuses[i][j] += 1
        
        has_flashed = True
        # While a flash occured.
        while has_flashed:
            has_flashed = False
            for i, line in enumerate(octopuses):
                for j, value in enumerate(line):
                    if value > 9 and (i, j) not in flashed_positions:
                        flashed_positions.add((i, j))
                        flash_count += 1
                        has_flashed = True
                        # Increment neighbours by 1. Max to 9
                        for neighbour in find_neighbours(i, j, octopuses):
                            octopuses[neighbour[0]][neighbour[1]] += 1
        
        for position in flashed_positions:
            octopuses[position[0]][position[1]] = 0

        if iteration == 100:
            print(f'part_1={flash_count}')
        
        if len(flashed_positions) == len(octopuses) * len(octopuses[0]):
            print(f'part_2={iteration}')
            return
        
        iteration += 1

if __name__ == '__main__':
    print('2021 day 11')
    solve()
