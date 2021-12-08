
digit_0 = 'abcefg'
digit_1 = 'cf'
digit_2 = 'acdeg'
digit_3 = 'acdfg'
digit_4 = 'bcdf'
digit_5 = 'abdfg'
digit_6 = 'abdefg'
digit_7 = 'acf'
digit_8 = 'abcdefg'
digit_9 = 'abcdfg'

all_digits = [digit_0, digit_1, digit_2, digit_3, digit_4, digit_5, digit_6, digit_7, digit_8, digit_9]

def part_1():
    inputs = []
    outputs = []
    with open('2021/8/input', 'r') as f:
        for line in f.readlines():
            in_out = line.strip().split('|')
            inputs.append(in_out[0].split())
            outputs.append(in_out[1].split())

    count = 0
    for output in outputs:
        for digit in output:
            if len(digit) in [2, 4, 3, 7]:
                count += 1

    return count

def map_string(digit, mapping):
    return ''.join(sorted([ mapping[ord(c) - ord('a')] for c in digit ]))

def part_2():
    # Positions, [ 0 -> 8 ]
    import itertools

    inputs = []
    outputs = []
    with open('2021/8/input', 'r') as f:
        for line in f.readlines():
            in_out = line.strip().split('|')
            inputs.append(in_out[0].split())
            outputs.append(in_out[1].split())

    sum = 0
    # Just brute force. There aren't actually that many permutations (5040(?))
    for i in range(len(inputs)):
        input = inputs[i]
        for perm in list(itertools.permutations('abcdefg')):
            mapping = ''.join(perm) # mapping[i] = 'abcdefg'[i]
            success = True
            for digit in input:
                if map_string(digit, mapping) not in all_digits:
                    success = False
                    break
            if success:
                result_digit = ''
                for output_digit in outputs[i]:
                    result_digit += str(all_digits.index(map_string(output_digit, mapping)))

                sum += int(result_digit)
                break

    return sum

if __name__ == '__main__':
    print('2021 day 7')
    print(f'part_1={part_1()}')
    print(f'part_2={part_2()}')
