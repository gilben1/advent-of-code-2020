def get_seat_id(seat_code):
    row = 0
    min_row = 0
    max_row = 127
    mid_row = (max_row + min_row) / 2

    col = 0    
    min_col = 0
    max_col = 7
    mid_col = (max_col + min_col) / 2

    for c in seat_code:
        if c == 'F':
            row = max_row = mid_row
        elif c == 'B':  
            row = min_row = mid_row
        elif c == 'L':
            col = max_col = mid_col
        elif c == 'R':
            col = min_col = mid_col

        mid_row = (max_row + min_row) / 2
        mid_col = (max_col + min_col) / 2

    return ((row * 8) + col, row, col)

def get_seat_id2(seat_code):
    binary_code = seat_code.replace("F","0").replace("B","1").replace("L","0").replace("R","1")
    row = int(binary_code[0:7], 2)
    col = int(binary_code[7:10], 2)

    return row * 8 + col

def missing_seat(seat_code):
    
    return 0



with open("./input.txt", "r") as fp:
    input_string = fp.read()
    input_list = input_string.split("\n")

    result = list(map(get_seat_id2, input_list))
    result.sort()
    print(result)
    print(max(result))

    for i in range(min(result), max(result)):
        if not i in result:
            print(i)
