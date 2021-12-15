
# Find the low points.
# Low point is where adjacent points are higher.
# Find all the low points on the heightmap, add 1 and sum these.

def find_neighbour_positions(position, max_x, max_y):
    x = position[0]
    y = position[1]

    neighbours = []
    if x > 0:
        neighbours.append((x - 1, y))
    if y > 0:
        neighbours.append((x, y - 1))
    if x < max_x - 1:
        neighbours.append((x + 1, y))
    if y < max_y - 1:
        neighbours.append((x, y + 1))

    return neighbours

def get_value(position, map):
    return map[position[0]][position[1]]

def smoke_basin():
    with open('2021/9/input', 'r') as f:
        map = [ [ int(char) for char in line.strip() ]  for line in f.readlines() ]
    
    max_x = len(map)
    max_y = len(map[0])

    low_points = []

    part_1_sum = 0
    for i, line in enumerate(map):
        for j, num in enumerate(line):
            neighbours = find_neighbour_positions((i, j), max_x, max_y)

            if len(neighbours) == len([ p for p in neighbours if get_value(p, map) > num ]):
                low_points.append((i, j))
                part_1_sum += num + 1
    
    print(f'part_1={part_1_sum}')

    basin_sizes = []

    for low_point in low_points:
        search_points = set()
        search_points.add(low_point)
        found_points = set()
        found_points.add(low_point)

        while len(search_points) > 0:
            new_search_points = set()

            for search_point in search_points:
                neighbour_positions = find_neighbour_positions(search_point, max_x, max_y)
                search_point_value = get_value(search_point, map)

                for neighbour in neighbour_positions:
                    neighbour_value = get_value(neighbour, map)
                    if neighbour_value != 9 and neighbour_value > search_point_value:
                        # Part of the basin.
                        new_search_points.add(neighbour)

            search_points = new_search_points - found_points
            found_points = found_points | new_search_points

        basin_sizes.append(len(found_points))
    
    basin_sizes.sort()

    print(f'part_2={basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]}')

if __name__ == '__main__':
    print('2021 day 9')
    smoke_basin()
    
