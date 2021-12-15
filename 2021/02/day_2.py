
def part_1():
    horizontal_position = 0
    depth_position = 0

    with open('2021/2/input', 'r') as f:
        for line in f.readlines():
            splits = line.split()
            value = int(splits[1])
            if splits[0] == 'forward':
                horizontal_position += value
            elif splits[0] == 'down':
                depth_position += value
            elif splits[0] == 'up':
                depth_position -= value
    
    print(f"part_1={horizontal_position * depth_position}")

def part_2():
    horizontal_position = 0
    depth_position = 0
    aim = 0

    with open('2021/2/input', 'r') as f:
        for line in f.readlines():
            splits = line.split()
            value = int(splits[1])
            if splits[0] == 'forward':
                horizontal_position += value
                depth_position += value * aim
            elif splits[0] == 'down':
                aim += value
            elif splits[0] == 'up':
                aim -= value

    print(f"part_2={horizontal_position * depth_position}")

if __name__ == "__main__":
    print('2021 day 2')
    part_1()
    part_2()
