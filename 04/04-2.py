import re

def validate_byr(value):
    return len(value) == 4 and 1920 <= int(value) and int(value) <= 2002

def validate_iyr(value):
    return len(value) == 4 and 2010 <= int(value) and int(value) <= 2020

def validate_eyr(value):
    return len(value) == 4 and 2020 <= int(value) and int(value) <= 2030

def validate_hgt(value):
    if "cm" in value:
        height = int(value.split("cm")[0])
        return 150 <= height and height <= 193
    elif "in" in value:
        height = int(value.split("in")[0])
        return 59 <= height and height <= 76
    else:
        return False


def validate_hcl(value):
    return re.search(r'#[0-9a-f]{6}', value) != None and len(value) == 7

def validate_ecl(value):
    return re.search(r'amb|blu|brn|gry|grn|hzl|oth', value) != None and len(value) == 3

def validate_pid(value):
    return re.search(r'\d{9}', value) != None and len(value) == 9

validate_map = {
    "byr": validate_byr,
    "iyr": validate_iyr,
    "eyr": validate_eyr,
    "hgt": validate_hgt,
    "hcl": validate_hcl,
    "ecl": validate_ecl,
    "pid": validate_pid
}

def valid_passport(passport):

    for key in validate_map:
        splitter = key + ":"
        val = passport.split(splitter)
        if len(val) != 1:
            val = re.split(r'\s',val[1])[0]
            if not validate_map[key](val):
                return False
        else:
            return False
    return True

def valid_passport_old(passport):
    expected = [
        (r'byr:(19[2-9][0-9]|200[0-2])', 8),
        (r'iyr:(201[0-9]|2020)', 8),
        (r'eyr:(202[0-9]|2030)', 8),
        (r'hgt:(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))', -1),
        (r'hcl:#[0-9a-f]{6}', 11),
        (r'ecl:(amb|blu|brn|gry|grn|hzl|oth)', 7),
        (r'pid:[0-9]{9}', 13)
    ]

    for val in expected:
        regex = val[0]
        length = val[1]
        search = re.search(regex, passport)
        
        if search == None:
            return False
        elif length != -1 and len(search.group(0)) != length:
            return False
    return True

with open("./input.txt", "r") as fp:
    input_string = fp.read()
    input_list = input_string.split("\n\n")

    results = list(map(valid_passport, input_list))

    print(results.count(True))
    print(len(results))