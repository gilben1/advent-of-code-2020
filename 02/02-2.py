import re

def parse_line(line):
    # pull out the upper and lower bounds
    first_index,second_index = map(int, re.findall(r'\d+', line))
    key = line.split(' ')[1][0]
    password = line.split(' ')[2]

    return first_index,second_index,key,password

def valid_pass_unpack(tup):
    return valid_pass(*tup)

def valid_pass(first_index, second_index, key, password):
    if first_index - 1 >= len(password) or second_index - 1 >= len(password):
        return False

    first_char = password[first_index - 1] == key
    second_char = password[second_index - 1] == key
    return first_char ^ second_char

with open("./input.txt", "r") as fp:
    input_string = fp.read()
    input_list = input_string.split('\n')
    input_list.pop()

    parse_results = list(map(parse_line, input_list))

    password_results = list(map(valid_pass_unpack, parse_results))

    print(password_results.count(True))    