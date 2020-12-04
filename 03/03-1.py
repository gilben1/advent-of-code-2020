def is_tree(line, index):
    return line[index] == '#'

with open("./input.txt", "r") as fp:
    input_string = fp.read()
    input_list = input_string.split('\n')
    input_list.pop()


    index = 0
    max_index = len(input_list[0])
    trees = 0

    for line in input_list:
        if is_tree(line, index):
            trees += 1
        index = (index + 3) % max_index
    
    print(trees)