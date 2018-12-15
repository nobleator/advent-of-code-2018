import numpy as np


def d11_1(serial_number):
    def power(x, y):
        rack_id = (x + 10)
        return ((((y * rack_id) + serial_number) * rack_id) // 100 % 10) - 5
    matrix = np.array([[power(x, y) for x in range(1, 301)] for y in range(1, 301)])
    max_value = 0
    max_coord = None
    for x in range(297):
        for y in range(297):
            value = np.sum(matrix[y:y + 3, x:x + 3])
            if value > max_value:
                max_value = value
                max_coord = (x + 1, y + 1)
    return max_coord, max_value

def d11_2(serial_number):
    def power(x, y):
        rack_id = (x + 10)
        return ((((y * rack_id) + serial_number) * rack_id) // 100 % 10) - 5
    matrix = np.array([[power(x, y) for x in range(1, 301)] for y in range(1, 301)])
    max_value = 0
    max_coord = None
    max_sq_size = 1
    for x in range(300):
        for y in range(300):
            for sq_size in range(300 - max(x, y)):
                value = np.sum(matrix[y:y + sq_size, x:x + sq_size])
                if value > max_value:
                    max_value = value
                    max_coord = (x + 1, y + 1)
                    max_sq_size = sq_size
    return max_coord, max_sq_size, max_value

# My input
# with open("d11.txt", "r") as f:
#     data = "".join(f.readlines())
#     data = data.rstrip("\n")

# Part 1
# Test cases
print(f"Expected {(33,45)} and got {d11_1(18)}")
print(f"Expected {(21,61)} and got {d11_1(42)}")

print(f"Part 1 {d11_1(1955)}")

# Part 2
# Test cases
print(f"Expected {(90,269,16)} and got {d11_2(18)}")
print(f"Expected {(232,251,12)} and got {d11_2(42)}")

print(f"Part 2 {d11_2(1955)}")
