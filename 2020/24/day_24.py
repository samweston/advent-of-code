
# Assuming unit equilateral triangles make up the
# hexagon:

# W/E movements occur in 1/2(root(3)) movements
# N/S movements occur in 1.5 movements

# W = (+2, +0)
# E = (-2, +0)
# SW = (1, -1.5)
# SE = (-1, -1.5)
# NW = (1, 1.5)
# NE = (-1, 1.5)

def we_direction(d):
    if d == 'w':
        return 1
    elif d == 'e':
        return -1
    else:
        raise Exception('Unexpected direction')

def nw_direction(d):
    if d == 'n':
        return 1
    elif d == 's':
        return -1
    else:
        raise Exception('Unexpected direction')

def neighbours(position):
    return [ (pos[0] + position[0], pos[1] + position[1]) for pos in  [(2, 0), (-2, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)] ]

def black_tiles(tiles):
    return dict(filter(lambda v: v[1] % 2 == 1, tiles.items())).keys()

def main():
    with open('2020/24/input', 'r') as f:
        lines = [ line.strip() for line in f.readlines() ]
    
    tiles = dict()

    for line in lines:
        x = 0
        y = 0

        i = 0
        while i < len(line):
            if line[i] in ('w', 'e'):
                x += we_direction(line[i]) * 2
            elif line[i] in ('n', 's'):
                y += nw_direction(line[i])
                x += we_direction(line[i + 1])
                i += 1
            else:
                raise Exception('Unexpected direction')
            i += 1
        
        if (x, y) not in tiles:
            tiles[(x, y)] = 0
        tiles[(x, y)] += 1

    print(f"part_1={len(black_tiles(tiles))}")

    # black tile with 0 or >2 black neighbours -> white
    # white tile with 2 black neighbours -> black

    curr_black_tiles = set(black_tiles(tiles))

    for i in range(0, 100):
        black_neighbour_counts = dict()

        # Calculate neighbour counts.
        for black_tile in curr_black_tiles:
            for neighbour in neighbours(black_tile):
                if neighbour not in black_neighbour_counts:
                    black_neighbour_counts[neighbour] = 0
                black_neighbour_counts[neighbour] += 1
        
        new_black_tiles = set()

        for black_tile in curr_black_tiles:
            if black_tile in black_neighbour_counts and black_neighbour_counts[black_tile] in (1, 2):
                # Remaining black tiles
                new_black_tiles.add(black_tile)

        for w_tile in black_neighbour_counts.keys():
            if black_neighbour_counts[w_tile] == 2:
                if w_tile not in curr_black_tiles:
                    new_black_tiles.add(w_tile)
        
        curr_black_tiles = new_black_tiles
    
    print(f"part_2={len(curr_black_tiles)}")


if __name__ == "__main__":
    print('2020 day 24')
    main()
