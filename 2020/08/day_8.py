
def run_instructions(instructions):
    accumulator = 0
    program_counter = 0

    visited_instructions = set()

    while True:
        if program_counter in visited_instructions:
            return (False, accumulator)
        elif program_counter >= len(instructions):
            return (True, accumulator)

        visited_instructions.add(program_counter)

        if instructions[program_counter][0] == 'acc':
            accumulator += instructions[program_counter][1]
            program_counter += 1
        elif instructions[program_counter][0] == 'jmp':
            program_counter += instructions[program_counter][1]
        elif instructions[program_counter][0] == 'nop':
            program_counter += 1
        else:
            raise Exception("Unexpected instruction")

def part_1():
    with open('2020/8/input', 'r') as f:
        instructions = [ (val.split()[0], int(val.split()[1])) for val in f.readlines() ]
    
    _, accumulator = run_instructions(instructions)
    return accumulator

def part_2():
    with open('2020/8/input', 'r') as f:
        instructions = [ (val.split()[0], int(val.split()[1])) for val in f.readlines() ]
    
    for i in range(len(instructions)):
        original = instructions[i]
        if instructions[i][0] in ['nop', 'jmp']:
            if instructions[i][0] == 'nop':
                instructions[i] = ('jmp', instructions[i][1])
            elif instructions[i][0] == 'jmp':
                instructions[i] = ('nop', instructions[i][1])
            
            completed, accumulator = run_instructions(instructions)
            if completed:
                return accumulator
        
        instructions[i] = original


if __name__ == "__main__":
    print('2020 day 8')
    print(f"part_1={part_1()}")
    print(f"part_2={part_2()}")
