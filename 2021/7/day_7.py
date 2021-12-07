

def find_best_cost(high_costs):
    with open("2021/7/input", 'r') as f:
        positions = [ int(num) for num in f.readline().split(',') ]
    
    min_num = min(positions)
    max_num = max(positions)

    if high_costs:
        costs = []
        total_cost = 0
        for i in range(0, max_num + 1):
            costs.append(i + total_cost)
            total_cost += i 

    best_score = float('inf')
    best_position = -1
    for i in range(min_num, max_num):
        score = 0
        for num in positions:
            if high_costs:
                score += costs[abs(num - i)]
            else:
                score += abs(num - i)
        
        if score < best_score:
            best_score = score
            best_position = i

    return best_score



if __name__ == "__main__":
    print('2021 day 7')
    print(f"part_1={find_best_cost(False)}")
    print(f"part_2={find_best_cost(True)}")
    
