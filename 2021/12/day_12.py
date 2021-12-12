
# big caves (uppercase) - visit any number of times.
# small caves (lowercase) - visit once

from collections import defaultdict

def count_paths_1(nodes, current_node, visited_count):
    if current_node == 'end':
        return 1
    
    count = 0
    for next_node in nodes[current_node]:
        if (next_node != 'start') and \
                (next_node.isupper() or visited_count[next_node] == 0):

            visited_count[next_node] += 1
            count += count_paths_1(nodes, next_node, visited_count)
            visited_count[next_node] -= 1
    
    return count

# Checking this at every step is slow. W/e I guess.
def countains_lower_double(visited_count):
    for item in visited_count:
        if item.islower() and visited_count[item] >= 2:
            return True
    return False
    
def count_paths_2(nodes, current_node, visited_count):
    if current_node == 'end':
        return 1
    
    count = 0
    for next_node in nodes[current_node]:
        if (next_node != 'start') and \
                (next_node.isupper() or visited_count[next_node] == 0 or not countains_lower_double(visited_count)):
            visited_count[next_node] += 1
            count += count_paths_2(nodes, next_node, visited_count)
            visited_count[next_node] -= 1
    
    return count

def solve():
    nodes = defaultdict(lambda: [])
    with open('2021/12/input', 'r') as f:
        for line in f.readlines():
            splits = line.strip().split('-')
            
            nodes[splits[0]].append(splits[1])
            nodes[splits[1]].append(splits[0])

    visited_count = defaultdict(lambda: 0)

    part_1_count = count_paths_1(nodes, 'start', visited_count)
    print(f'part_1={part_1_count}')
    part_2_count = count_paths_2(nodes, 'start', visited_count)
    print(f'part_2={part_2_count}')
    
if __name__ == '__main__':
    print('2021 day 11')
    solve()