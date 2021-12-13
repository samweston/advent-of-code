
# Instructions on how to fold up
# 0,0 = top left. x,y. These are dots

# Fold instructions

# 10, with fold 7 => 4

def apply_fold(coords, fold):
    new_coords = set()
    for coord in coords:
        if fold[0] == 'x':
            # new_x = fold_x - (old_x - fold_x) = 2 * fold_x - old_x
            if coord[0] > fold[1]:
                new_coords.add( (fold[1] * 2 - coord[0], coord[1]) )
            else:
                new_coords.add( coord )
        elif fold[0] == 'y':
            if coord[1] > fold[1]:
                new_coords.add( (coord[0], fold[1] * 2 - coord[1]) )
            else:
                new_coords.add( coord )
        else:
            raise Exception('unexpected fold')

    return new_coords

def print_coords(coords):
    min_x = min([ coord[0] for coord in coords ])
    max_x = max([ coord[0] for coord in coords ])
    min_y = min([ coord[1] for coord in coords ])
    max_y = max([ coord[1] for coord in coords ])

    for y in range(min_y, max_y + 1):
        line = ''
        for x in range(min_x, max_x + 1):
            if (x, y) in coords:
                line += '#'
            else:
                line += ' '
        print(line)

def read_coords_and_folds():
    coords = set() # (x, y)
    folds = []     # ('x'/'y', fold_position)
    with open('2021/13/input', 'r') as f:
        lines = [ line.strip() for line in f.readlines() ]
        mid = lines.index('')

        for line in lines[0:mid]:
            splits = line.split(',')
            coords.add( (int(splits[0]), int(splits[1])) )
        
        for line in lines[mid + 1::]:
            splits = line.split('=')
            folds.append( (splits[0][-1], int(splits[1])) )

    return coords, folds

def part_1():
    coords, folds = read_coords_and_folds()
    
    new_coords = apply_fold(coords, folds[0])

    return len(new_coords)

def part_2():
    coords, folds = read_coords_and_folds()
    
    for fold in folds:
        coords = apply_fold(coords, fold)
    
    print('part_2=')
    print_coords(coords)


if __name__ == '__main__':
    print('2021 day 13')
    print(f'part_1={part_1()}')
    part_2()
