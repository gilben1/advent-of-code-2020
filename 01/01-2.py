with open("./input.txt", "r") as fp:
    input_string = fp.read()
    input_list = input_string.split('\n')
    input_list.pop()

    inputs = list(map(lambda x: int(x), input_list))

    for x in inputs:
        for y in inputs:
            find = 2020 - x - y
            if find in inputs:
                print(x * y  * find)