def process_all(lines,slope):
    right = slope[0]
    down = slope[1]

    index = 0 
    max_index = len(input_list[0])
    trees = 0

    for line in lines:
        trees += process_slope(line, index)
        index = (index + right) % max_index
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

    print(process_all(input_list, (3,1)))