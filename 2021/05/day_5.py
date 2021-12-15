
# x1,y1 -> x2,y2

def intersections(include_diagonal):
    counts = dict()

    with open('2021/5/input', 'r') as f:
        for line in f.readlines():
            splits = line.split()
            x1 = int(splits[0].split(',')[0])
            y1 = int(splits[0].split(',')[1])
            x2 = int(splits[2].split(',')[0])
            y2 = int(splits[2].split(',')[1])

            inc_x = 0
            inc_y = 0

            if (x1 != x2):
                inc_x = (x2 - x1) // abs(x2 - x1)
            
            if (y1 != y2):
                inc_y = (y2 - y1) // abs(y2 - y1)

            max_diff = max(abs(x2 - x1), abs(y2 - y1))

            if (include_diagonal or x1 == x2 or y1 == y2):
                for i in range(0, max_diff + 1):
                    new_pos = (x1, y1)
                    if new_pos not in counts:
                        counts[new_pos] = 0
                    counts[new_pos] += 1
                    x1 += inc_x
                    y1 += inc_y
    
    total = 0
    for position in counts:
        if counts[position] > 1:
            total += 1
    
    return total


if __name__ == "__main__":
    print('2021 day 5')
    print(f"part1={intersections(False)}")
    print(f"part2={intersections(True)}")
