
def load_data(path:str) -> tuple[list, list]:
    patterns = []
    digits = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip("\n").split(" | ")

            pat = line[0].strip(" ").split(" ")
            patterns.append(pat)

            dig = line[1].strip(" ").split(" ")
            digits.append(dig)

    return patterns, digits


def count_simple_digits(digits:list) -> int:
    unique = [2, 3, 4, 7]  # Number of segments of numbers with unique number of segments (1, 7, 4 and 8, respectively)
    count = 0
    for d in digits:
        for i in d:
            if len(i) in unique:
                count += 1
    return count


"""
NOTES

# Number of segments that each number has
n_segm = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

# Number of times that each segment appears
segm_count = {
    "a": 8,
    "b": 6,
    "c": 8,
    "d": 7,
    "e": 4,
    "f": 9,
    "g": 7
}

# Number of times that each segment appears in the complex numbers 
segm_count_upd = {
    "a": 6,
    "b": 4,
    "c": 6,
    "d": 5,
    "e": 3,
    "f": 5,
    "g": 6
}
# Numbers depending on the number of segments:
# 2 segments: 1
# 3 segments: 7
# 4 segments: 4
# 5 segments: 2, 3, 5
# 6 segments: 0, 6, 9
# 7 segments: 8
#
# Algorithms to find numbers
# 3 is the only 5-segment number that contains the two segments of 1
# 9 is the only 6-segment number that contains the four segments of 4
# 2 is the only number that does not contain the "f" segment
# 6 is the only 6-segment number that does not contain both of the two segments of 1
# 0 is the only number (with 1 and 7) that does not contain the center segment
"""


def crack_code(patterns:list) -> dict:
    code = {}
    inv_code = {}

    # Get easy numbers
    for pat in patterns:
        num = None
        if len(pat) == 2:
            num = 1
        elif len(pat) == 3:
            num = 7
        elif len(pat) == 4:
            num = 4
        elif len(pat) == 7:
            num = 8
        else:
            # We don't know the number yet
            continue

        if num:
            pat = "".join(sorted(pat))
            code[pat] = num
            inv_code[num] = pat

    # TODO: Avoid iterating twice over patterns by using a queue
    for pat in patterns:
        num = None
        if len(pat) == 5:
            # 3 is the only 5-segment number that contains the two segments of 1
            if inv_code[1][0] in pat and inv_code[1][1] in pat:
                num = 3

            # If it is not 3, 5 is the only 5-segment number that contains three segments of 4
            elif sum([inv_code[4][x] in pat for x in range(4)]) == 3:  # One line expression to test whether 3 of the segments of 4 are present in pat
                num = 5

            else:
                num = 2

        elif len(pat) == 6:
            # 6 is the only 6-segment number that does not contain both of the two segments of 1
            if inv_code[1][0] not in pat or inv_code[1][1] not in pat:
                num = 6

            # 9 is the only 6-segment number that contains the four segments of 4
            elif min([inv_code[4][x] in pat for x in range(4)]):  # One line expression to test whether all 4 segments of 4 are present in pat
                num = 9

            else:
                num = 0

        if num is not None:
            pat = "".join(sorted(pat))
            code[pat] = num
            inv_code[num] = pat

    return code


def solve_electric_problem(all_patterns:list, all_digits:list) -> int:
    solution = 0
    for c, patterns in enumerate(all_patterns):
        code = crack_code(patterns)
        number = ""
        for d in all_digits[c]:
            d = "".join(sorted(d))
            number += str(code[d])

        number = int(number)
        solution += number
    return solution


if __name__ == "__main__":
    all_patterns, all_digits = load_data("input.txt")
    print(count_simple_digits(all_digits))
    print(solve_electric_problem(all_patterns, all_digits))
