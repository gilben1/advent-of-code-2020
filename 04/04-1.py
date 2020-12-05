def valid_passport(passport):
    expected = ["byr:", "iyr:","eyr:","hgt:","hcl:","ecl:","pid:"]

    for val in expected:
        if passport.find(val) == -1:
            return False
    return True

with open("./input.txt", "r") as fp:
    input_string = fp.read()
    input_list = input_string.split("\n\n")


    results = list(map(valid_passport, input_list))
    print(results)
    print(results.count(True))