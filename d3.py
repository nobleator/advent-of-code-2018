import numpy as np
import time


def d3_1_numpy(data):
    data = data.split("\n")
    mat = np.zeros((2500, 2500))
    for row in data:
        claim_id, _, offset, dimensions = row.split(" ")
        (x_offset, y_offset) = [int(e) for e in offset.rstrip(":").split(",")]
        (width, height) = [int(e) for e in dimensions.split("x")]
        mat[y_offset:y_offset + height, x_offset:x_offset + width] += 1
    return len(mat[np.where(mat > 1)])

def d3_1_dict(data):
    # Not working, too high (Numpy version is correct)
    data = data.split("\n")
    # Dictionary does not require pre-allocating space, but requires explicit iterations over sub-grids
    grid = {}
    for row in data:
        claim_id, _, offset, dimensions = row.split(" ")
        (y_offset, x_offset) = [int(e) for e in offset.rstrip(":").split(",")]
        (width, height) = [int(e) for e in dimensions.split("x")]
        for x in range(x_offset, x_offset + width):
            for y in range(y_offset, y_offset + width):
                if (x, y) not in grid:
                    grid[x, y] = 1
                else:
                    grid[x, y] += 1
    return len([elem for elem in grid if grid[elem] > 1])

def d3_2(data):
    data = data.split("\n")
    mat = np.zeros((2500, 2500))
    intact_claim = "NO INTACT CLAIM"
    for row in data:
        claim_id, _, offset, dimensions = row.split(" ")
        (x_offset, y_offset) = [int(e) for e in offset.rstrip(":").split(",")]
        (width, height) = [int(e) for e in dimensions.split("x")]
        mat[y_offset:y_offset + height, x_offset:x_offset + width] += 1
    for row in data:
        claim_id, _, offset, dimensions = row.split(" ")
        (x_offset, y_offset) = [int(e) for e in offset.rstrip(":").split(",")]
        (width, height) = [int(e) for e in dimensions.split("x")]
        if np.all(mat[y_offset:y_offset + height, x_offset:x_offset + width] == 1):
            intact_claim = claim_id
    return intact_claim

# My input
with open("d3.txt", "r") as f:
    data = "".join(f.readlines())
    data = data.rstrip("\n")

# Part 1
# Test cases
test_input = "#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2"
print(f"With dict: expected {4} and got {d3_1_dict(test_input)}")
print(f"With Numpy: expected {4} and got {d3_1_numpy(test_input)}")
test_input = "#1 @ 1,3: 4x4\n#2 @ 1,3: 4x4"
print(f"With dict: expected {16} and got {d3_1_dict(test_input)}")
print(f"With Numpy: expected {16} and got {d3_1_numpy(test_input)}")
test_input = "#1 @ 1,1: 2x2\n#2 @ 0,4: 4x4"
print(f"With dict: expected {0} and got {d3_1_dict(test_input)}")
print(f"With Numpy: expected {0} and got {d3_1_numpy(test_input)}")


start = time.time()
res = d3_1_dict(data)
print(f"Part 1 {res} with dict took {time.time() - start} seconds")
start = time.time()
res = d3_1_numpy(data)
print(f"Part 1 {res} with numpy took {time.time() - start} seconds")

# Part 2
# Test cases
test_input = "#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2"
print(f"Expected {3} and got {d3_2(test_input)}")

print(f"Part 2 {d3_2(data)}")

