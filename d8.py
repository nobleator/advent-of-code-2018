
def get_tail_and_meta(data, head):
    # Recursive approach fails on real data due to max recursion depth
    num_children = data[head]
    num_metadata = data[head + 1]
    if num_children == 0:
        peer_head = head + num_metadata + 2
        meta = sum(data[n] for n in range(head + 2, head + num_metadata + 2))
        # print(f"No children, head {head}, peer head {peer_head}, meta {meta}")
        return peer_head, meta
    else:
        meta = 0
        child_head = head + 2
        for child in range(num_children):
            # print(f"Child {child} of {num_children}, head {head}, child head {child_head}, meta {meta}")
            child_head, child_meta = get_tail_and_meta(data, child_head)
            meta += child_meta
        meta += sum(data[n] for n in range(child_head, child_head + num_metadata))
        return child_head, meta

def recurse_1(data):
    # This version modifies the data list directly
    num_children, num_metadata = data[:2]
    data = data[2:]
    meta = 0
    for child in range(num_children):
        data, child_meta = recurse_1(data)
        meta += child_meta
    meta += sum(data[:num_metadata])
    return data[num_metadata:], meta

def recurse_2(data):
    # This version modifies the data list directly
    num_children, num_metadata = data[:2]
    data = data[2:]
    child_values = []
    for child in range(num_children):
        data, child_value = recurse_2(data)
        child_values.append(child_value)
    if num_children == 0:
        value = sum(data[:num_metadata])
    else:
        value = 0
        for m in data[:num_metadata]:
            if 0 < m <= len(child_values):
                value += child_values[m - 1]
    return data[num_metadata:], value

def d8_1(data):
    data = [int(e) for e in data.split(" ")]
    # return get_tail_and_meta(data, 0)
    return recurse_1(data)

def d8_2(data):
    data = [int(e) for e in data.split(" ")]
    return recurse_2(data)

# My input
with open("d8.txt", "r") as f:
    data = "".join(f.readlines())
    data = data.rstrip("\n")

# Part 1
# Test cases
test_input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
print(f"Expected {138} and got {d8_1(test_input)}")

res = d8_1(data)
print(f"Part 1 {res}")

# Part 2
# Test cases
test_input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
print(f"Expected {66} and got {d8_2(test_input)}")

print(f"Part 2 {d8_2(data)}")
