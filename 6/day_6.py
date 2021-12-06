# Each lantern fish -> new one every 7 days
# 2 extra days for first cycle

# timer. Start 1
# another day -> 0
# another day -> 6. + lanternfish with 8

def num_lanternfish(days):
    with open('6/input', 'r') as f:
        fish = [ int(n) for n in f.read().split(',') ]
    
    buckets = [0] * 9
    for f in fish:
        buckets[f] += 1

    for i in range(0, days):
        new_fish = buckets[0]
        for j in range(0, 8):
            buckets[j] = buckets[j + 1]
        buckets[8] = new_fish
        buckets[6] += new_fish

    return sum(buckets)

if __name__ == "__main__":
    print('day 6')
    print(f"part_1={num_lanternfish(80)}")
    print(f"part_2={num_lanternfish(256)}")
