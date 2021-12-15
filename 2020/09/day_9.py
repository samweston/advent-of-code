
# Input = series of numbers. Encrypted with XMAS.
# Preamble = 25 numbers.
# After, each number is sum of any of 2 of any previous 25 numbers.
#   - 2 numbers are different, may be more than one such pair 

def run_decrypt():
    preamble_count = 25

    with open('2020/9/input', 'r') as f:
        nums = [ int(line) for line in f.readlines() ]
    
    available_nums = []
    for i in range(preamble_count):
        available_nums.append(nums[i])
    
    part_1_num = 0

    for i in range(preamble_count, len(nums)):
        num = nums[i]
        found = False
        for j, num1 in enumerate(available_nums):
            if (num - num1) in [ num2 for k, num2 in enumerate(available_nums) if j != k ]:
                found = True
                break

        if not found:
            part_1_num = num
            print(f'part_1={num}')
            break
        
        del available_nums[0]
        available_nums.append(num)
    
    for i, start_num in enumerate(nums):
        sum = start_num
        smallest = largest = start_num
        for j in range(i + 1, len(nums)):
            sum += nums[j]
            largest = max(largest, nums[j])
            smallest = min(smallest, nums[j])

            if sum == part_1_num:
                print(f'part_2={smallest + largest}')
                return
            elif sum > part_1_num:
                break

if __name__ == '__main__':
    print('2020 day 9')
    run_decrypt()
