import difflib


def d2_1(data):
    data = data.split("\n")
    total_nums = {2: 0, 3: 0}
    for row in data:
        two_found = False
        three_found = False
        for char in row:
            num = row.count(char) 
            if not two_found and num == 2:
                total_nums[2] += 1
                two_found -= True
            if not three_found and num == 3:
                total_nums[3] += 1
                three_found = True
    return total_nums[2] * total_nums[3]

def verify_and_return_similar(s1, s2):
    result = []
    diff_found = False
    char_indx = 0
    while char_indx < min(len(s1), len(s2)):
        if s1[char_indx] != s2[char_indx]:
            if diff_found:
                return False, ""
            else:
                diff_found = True
        else:
            result.append(s1[char_indx])
        char_indx += 1
    return True, "".join(result)

def d2_2(data):
    result = "ERROR ERROR NO MATCH"
    data = data.split("\n")
    row_indx = 0
    while row_indx < len(data) - 1:
        sub = data[:row_indx] + data[row_indx + 1:]
        match = difflib.get_close_matches(data[row_indx], sub, 1, 0.8)
        if len(match) > 0:
            true_match, similar = verify_and_return_similar(data[row_indx], match[0])
            if true_match:
                result = similar
        row_indx += 1
    return result

# My input
with open("d2.txt", "r") as f:
    data = "".join(f.readlines())
    data = data.rstrip("\n")

# Part 1
# Test cases
test_input = "abcdef\nbababc\nabbcde\nabcccd\naabcdd\nabcdee\nababab\n"
print(f"Expected {12} and got {d2_1(test_input)}")

print(f"Part 1 {d2_1(data)}")

# Part 2
# Test cases
test_input = "abcde\nfghij\nklmno\npqrst\nfguij\naxcye\nwvxyz\n"
print(f"Expected {'fgij'} and got {d2_2(test_input)}")

print(f"Part 2 {d2_2(data)}")

