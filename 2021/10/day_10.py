
# Navigation system = input
# Lines may be incomplete or corrupted.
# Discard corrupted lines first. corrupted -> closes with wrong character.
# (), [], {}, <>
# ) = 3, ] = 57, } = 1197, > = 25137. First illegal charcater.

def parse_line(line, return_invalid):
    stack = []
    opens = [ '(', '[', '{', '<']
    closes = [ ')', ']', '}', '>' ]
    invalid_values = [ 3, 57, 1197, 25137 ]
    incomplete_values = [ 1, 2, 3, 4 ]

    for character in line:
        if character in opens:
            stack.append(opens.index(character))
        elif character in closes:
            expected = stack.pop()
            current = closes.index(character)
            if expected != current:
                if return_invalid:
                    return invalid_values[current]
                else:
                    return -1
        else:
            raise Exception(f'Invalid character - {character}')
    
    score = 0
    if not return_invalid:
        for item in reversed(stack):
            score *= 5
            score += incomplete_values[item]
        
    return score

def solve():
    with open('2021/10/input', 'r') as f:
        lines = [ line.strip() for line in f.readlines() ]
    
    invalid_score = 0
    for line in lines:
        invalid_score += parse_line(line, True)
    
    print(f'part_1={invalid_score}')
    
    all_scores = []
    for line in lines:
        score = parse_line(line, False)
        if score != -1:
            all_scores.append(score)
    
    all_scores.sort()
    print(f'part_2={all_scores[len(all_scores) // 2]}')

if __name__ == '__main__':
    print('2021 day 10')
    solve()
