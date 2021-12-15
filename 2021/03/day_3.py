
EQUAL_STRING = 'equal'

def find_most_common(bit_nums, position):
    one_count = 0
    for bit_num in bit_nums:
        if bit_num[position] == '1':
            one_count += 1
    if one_count >= (len(bit_nums) / 2):
        return '1'
    else:
        return '0'

def part_1():
    # Gamma rate. Most common bits
    with open('2021/3/input', 'r') as f:
        bit_nums = f.readlines()

    gamma_string = ''
    epsilon_string = ''
    for i in range(0, len(bit_nums[0]) - 1):
        if find_most_common(bit_nums, i) == '1':
            gamma_string += '1'
            epsilon_string += '0'
        else:
            gamma_string += '0'
            epsilon_string += '1'
    
    gamma = int(gamma_string, 2)
    epsilon = int(epsilon_string, 2)

    print(f"{gamma_string},{epsilon_string}")
    print(f"{gamma},{epsilon}")
    print(f"part_1={gamma * epsilon}")

def part_2():
    with open('2021/3/input', 'r') as f:
        bit_nums = f.readlines()

    bit_count = len(bit_nums[0]) - 1
    oxygen_bit_nums = bit_nums.copy()
    co2_bit_nums = bit_nums.copy()

    for i in range(0, bit_count):
        most_common = find_most_common(oxygen_bit_nums, i)
        if len(oxygen_bit_nums) > 1:
            oxygen_bit_nums = [ bit_num for bit_num in oxygen_bit_nums if bit_num[i] == most_common ]

    for i in range(0, bit_count):
        most_common = find_most_common(co2_bit_nums, i)
        if len(co2_bit_nums) > 1:
            co2_bit_nums = [ bit_num for bit_num in co2_bit_nums if bit_num[i] != most_common ]

    print(f"part_2={int(oxygen_bit_nums[0], 2) * int(co2_bit_nums[0], 2)}")

if __name__ == "__main__":
    print('2021 day 3')
    part_1()
    part_2()
