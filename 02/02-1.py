import re

def parse_line(line):
    # pull out the upper and lower bounds
    lower,upper = map(int, re.findall(r'\d+', line))
    key = line.split(' ')[1][0]
    password = line.split(' ')[2]

    return lower,upper,key,password

def valid_pass_unpack(tup):
    return valid_pass(*tup)

def valid_pass(lower, upper, key, password):
    count = password.count(key)
    return True if count >= lower and count <= upper else False

with open("./input.txt", "r") as fp:
    input_string = fp.read()
    input_list = input_string.split('\n')
    input_list.pop()

    parse_results = list(map(parse_line, input_list))

    password_results = list(map(valid_pass_unpack, parse_results))

    print(password_results.count(True))    