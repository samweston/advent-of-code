# hlf r              # Half
# tpl r              # Triple
# inc r
# jmp <offset>
# jie r, offset      # Jump if even
# jio r, offset      # Jump if 1

def get_register_index(reg):
    if reg[0] == 'a':
        return 0
    elif reg[0] == 'b':
        return 1
    raise Exception('Unexpected register')

def run_program(register_a, register_b):
    registers = [int(register_a), int(register_b)]
    
    program_counter = 0

    with open('2015/24/input', 'r') as f:
        lines = f.readlines()
        
    while(True):
        if (program_counter < 0) or (program_counter >= len(lines)):
            break

        line = lines[program_counter]
        splits = line.split()

        if splits[0] == 'hlf':
            registers[get_register_index(splits[1])] //= 2
            program_counter += 1
        elif splits[0] == 'tpl':
            registers[get_register_index(splits[1])] *= 3
            program_counter += 1
        elif splits[0] == 'inc':
            registers[get_register_index(splits[1])] += 1
            program_counter += 1
        elif splits[0] == 'jmp':
            program_counter += int(splits[1])
        elif splits[0] == 'jie':
            if registers[get_register_index(splits[1])] % 2 == 0:
                program_counter += int(splits[2])
            else:
                program_counter += 1
        elif splits[0] == 'jio':
            if registers[get_register_index(splits[1])] == 1:
                program_counter += int(splits[2])
            else:
                program_counter += 1
        else:
            raise Exception('Unexpected instruction')

        #print(f"{program_counter},{registers[0]},{registers[1]}")

    return registers[1] # b

if __name__ == "__main__":
    print('day 24')
    print(f"part_1={run_program(0, 0)}")
    print(f"part_2={run_program(1, 0)}")

