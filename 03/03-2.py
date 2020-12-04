def process_all(lines,slope):
    right = slope[0]
    down = slope[1]

    x = 0 
    max_x = len(input_list[0])
    trees = 0

    for y in range(0,len(input_list), down):
        trees += process_slope(input_list[y], x)
        x = (x + right) % max_x

    print(trees)
    return trees

def process_slope(line,index):
    if is_tree(line, index):
        return 1
    return 0

def is_tree(line, index):
    return line[index] == '#'

with open("./input.txt", "r") as fp:
    input_string = fp.read()
    input_list = input_string.split('\n')
    input_list.pop()

    total = 1
    total *= process_all(input_list, (1,1))
    total *= process_all(input_list, (3,1))
    total *= process_all(input_list, (5,1))
    total *= process_all(input_list, (7,1))
    total *= process_all(input_list, (1,2))
    print(total)