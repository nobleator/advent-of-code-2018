def d1_1(data):
    data = data.split(", ")
    return sum(int(elem) for elem in data)

def d1_2(data):
    data = data.split(", ")
    found = {0}
    frequency = 0
    elem_indx = 0
    while True:
        frequency += int(data[elem_indx])
        if frequency in found:
            return frequency
        else:
            found.add(frequency)
        elem_indx += 1
        if elem_indx >= len(data):
            elem_indx = 0

# My input
with open("d1.txt", "r") as f:
    data = "".join(f.readlines())
    # Replace newlines with commas so input matches test cases
    data = data.rstrip("\n").replace("\n", ", ")

# Part 1
# Test cases
print(f"Expected {3} and got {d1_1('+1, +1, +1')}")
print(f"Expected {0} and got {d1_1('+1, +1, -2')}")
print(f"Expected {-6} and got {d1_1('-1, -2, -3')}")

print(f"Part 1 {d1_1(data)}")

# Part 2
# Test cases
print(f"Expected {0} and got {d1_2('+1, -1')}")
print(f"Expected {10} and got {d1_2('+3, +3, +4, -2, -4')}")
print(f"Expected {5} and got {d1_2('-6, +3, +8, +5, -6')}")
print(f"Expected {14} and got {d1_2('+7, +7, -2, -7, -4')}")

print(f"Part 2 {d1_2(data)}")

