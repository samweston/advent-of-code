
# Charging outlet -> produced wrong number of jolts
# Joltage adapters are rated for a certain joltage.
#   - Can read 1, 2 or 3 jolts lower than rating.
# Also built-in joltage adapter 3 higher than highest rated adapter

def part_1():
    with open('2020/10/input', 'r') as f:
        adapters = [ int(line) for line in f.readlines() ]
    
    adapters.append(0)
    adapters.sort()

    ones = 0
    threes = 1
    for i in range(1, len(adapters)):
        diff = adapters[i] - adapters[i - 1]
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1
        else:
            print(diff)
    
    print(f'{ones},{threes}')
    return ones * threes

def part_2():
    with open('2020/10/input', 'r') as f:
        adapters = [ int(line) for line in f.readlines() ]
    
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()

    ways = dict()
    for val in adapters:
        ways[val] = 0
    ways[0] = 1

    for i, val in enumerate(adapters):
        current_ways = ways[val]
        for i in [1, 2, 3]:
            if val + i in ways:
                ways[val + i] += current_ways

    return ways[adapters[-1]]

if __name__ == '__main__':
    print('2020 day 10')
    print(f'part_1={part_1()}')
    print(f'part_2={part_2()}')
