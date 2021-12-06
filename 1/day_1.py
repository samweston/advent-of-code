

def part_1():
    prev = float('inf')
    count = 0
    with open('1/input', 'r') as f:
        for line in f.readlines():
            num = int(line)
            if num > prev:
                count += 1
            prev = num

    print(f"part_1={count}")

def part_2():
    count = 0

    with open('1/input', 'r') as f:
        lines = [ int(n) for n in f.readlines() ]

    prev = lines[0] + lines[1] + lines[2]
    for i in range(3, len(lines)):
        curr = lines[i] + lines[i - 1] + lines[i - 2]
        if curr > prev:
            count += 1
        prev = curr

    print(f"part_2={count}")

if __name__ == "__main__":
    part_1()
    part_2()

