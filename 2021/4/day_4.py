
def read_board(lines, index):
    rows = []
    for i in range(0, 5):
        rows.append([ int(num) for num in lines[index + i + 1].split() ])
    columns = []
    for i in range(0, 5):
        columns.append([ nums[i] for nums in rows])
    return (rows, columns)

def find_scores(numbers, boards):
    scores = []
    has_won = [False] * len(boards)

    for num in numbers:
        for i in range(0, len(boards)):
            board = boards[i]
            for rows_cols in board:
                for row_col in rows_cols:
                    if num in row_col:
                        row_col.remove(num)
                    if len(row_col) == 0 and not has_won[i]:
                        scores.append(num * sum(map(sum, rows_cols)))
                        has_won[i] = True
    
    return scores

def part_1_2():
    with open('2021/4/input', 'r') as f:
        numbers = [ int(num) for num in f.readline().split(',') ]
        board_strings = f.readlines()
    
    boards = []
    for i in range(0, len(board_strings), 6):
        rows, columns = read_board(board_strings, i)
        boards.append( (rows, columns) )
    
    scores = find_scores(numbers, boards)

    print(f"part_1={scores[0]}")
    print(f"part_2={scores[-1]}")


if __name__ == "__main__":
    print('2021 day 4')
    part_1_2()
