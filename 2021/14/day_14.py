
# instructions to find optimal polymer formula
#   has polymer template and a list of pair insertion rules (input)

#  AB -> C => ACB

from collections import defaultdict

def step(items, instructions):
    output = []

    for i in range(1, len(items)):
        current = items[i]
        previous = items[i - 1]
        if previous + current in instructions:
            output.append(previous)
            output.append(instructions[previous + current])
        else:
            output.append(previous)
    
    output.append(items[-1])

    return output

def read_input_and_instructions():
    instructions = dict()
    with open('2021/14/input', 'r') as f:
        input = list(f.readline().strip())
        f.readline()
        for line in f.readlines():
            splits = line.strip().split(' -> ')
            instructions[splits[0]] = splits[1]
    
    return input, instructions

def part_1():
    input, instructions = read_input_and_instructions()

    for i in range(0, 10):
        input = step(input, instructions)
    
    max_item = max(set(input), key=input.count)
    min_item = min(set(input), key=input.count)

    return input.count(max_item) - input.count(min_item)

def step_with_pairs(pair_counts, instructions):
    new_pair_counts = defaultdict(lambda: 0)

    for pair, count in pair_counts.items():
        if pair in instructions:
            new_pair_counts[pair[0] + instructions[pair]] += count
            new_pair_counts[instructions[pair] + pair[1]] += count
        else:
            new_pair_counts[pair] += count
    
    return new_pair_counts

def part_2():
    input, instructions = read_input_and_instructions()
    
    # Build the pair counts.
    pair_counts = defaultdict(lambda: 0)
    for i in range(len(input) - 1):
        pair_counts[input[i] + input[i + 1]] += 1

    for i in range(0, 40):
        pair_counts = step_with_pairs(pair_counts, instructions)

    # Find the counts for each item a pair count represent's
    # the first character in the pair's count. 
    counts = defaultdict(lambda: 0)
    for pair, count in pair_counts.items():
        counts[pair[0]] += count
    counts['B'] += 1 # B is always at the end

    sorted_counts = sorted(counts.items(), key=lambda item: item[1])
    return sorted_counts[-1][1] - sorted_counts[0][1]

if __name__ == '__main__':
    print('2021 day 14')
    print(f'part_1={part_1()}')
    print(f'part_2={part_2()}')  
