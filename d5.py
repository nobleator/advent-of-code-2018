import string


def d5_1(data):
    data = list(data)
    ctr = 0
    while ctr < len(data) - 1:
        char1 = data[ctr]
        char2 = data[ctr + 1]
        same_char = char1.lower() == char2.lower()
        diff_case = ((char1.islower() and char2.isupper()) 
                     or (char1.isupper() and char2.islower()))
        if same_char and diff_case:
            data.pop(ctr + 1)
            data.pop(ctr)
            ctr -= 1
            if ctr < 0:
                ctr = 0
        else:
            ctr += 1
    return len(data)

def d5_2(data):
    shortest = 50000
    for char in string.ascii_lowercase:
        res = d5_1("".join(e for e in data if e.lower() != char))
        if res < shortest:
            shortest = res
    return shortest

# My input
with open("d5.txt", "r") as f:
    data = "".join(f.readlines())
    data = data.rstrip("\n")

# Part 1
# Test cases
test_input = "aA"
print(f"Expected {0} and got {d5_1(test_input)}")
test_input = "abBA"
print(f"Expected {0} and got {d5_1(test_input)}")
test_input = "abAB"
print(f"Expected {4} and got {d5_1(test_input)}")
test_input = "aabAAB"
print(f"Expected {6} and got {d5_1(test_input)}")
test_input = "dabAcCaCBAcCcaDA"
print(f"Expected {10} and got {d5_1(test_input)}")


res = d5_1(data)
print(f"Part 1 {res}")

# Part 2
# Test cases
test_input = "dabAcCaCBAcCcaDA" 
print(f"Expected {4} and got {d5_2(test_input)}")

print(f"Part 2 {d5_2(data)}")
