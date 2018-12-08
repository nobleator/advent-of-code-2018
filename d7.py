def d7_1(data):
    data = data.split("\n")
    # precedences = {node1: [nodes that must be complete before node1 can begin]}
    precedences = {}
    nodes = set()
    completion_order = []
    for row in data:
        words = row.split(" ")
        head = words[1]
        tail = words[7]
        nodes.add(head)
        nodes.add(tail)
        if tail in precedences:
            precedences[tail].append(head)
        else:
            precedences[tail] = [head]
        if head not in precedences:
            precedences[head] = []
    while len(completion_order) < len(nodes):
        eligible_nodes = [n for n in sorted(nodes) if all(elem in completion_order for elem in precedences[n]) and n not in completion_order]
        completion_order.append(eligible_nodes[0])
    return "".join(completion_order)

def d7_2(data, num_workers, duration_offset):
    data = data.split("\n")
    # precedences = {node1: [nodes that must be complete before node1 can begin]}
    precedences = {}
    nodes = set()
    completion_order = []
    for row in data:
        words = row.split(" ")
        head = words[1]
        tail = words[7]
        nodes.add(head)
        nodes.add(tail)
        if tail in precedences:
            precedences[tail].append(head)
        else:
            precedences[tail] = [head]
        if head not in precedences:
            precedences[head] = []
    clock = 0
    completed_nodes = []
    nodes_in_progress = set()
    end_times = {}
    while len(completed_nodes) < len(nodes):
        for node in end_times:
            if clock >= end_times[node] and node in nodes_in_progress:
                nodes_in_progress.remove(node)
                completed_nodes.append(node)
        eligible_nodes = [n for n in sorted(nodes)
                          if all(elem in completed_nodes for elem in precedences[n])
                          and n not in completed_nodes
                          and n not in nodes_in_progress]
        for worker in range(num_workers - len(nodes_in_progress)):
            if len(eligible_nodes) > 0:
                node = eligible_nodes.pop(0)
                nodes_in_progress.add(node)
                end_times[node] = clock + ord(node.lower()) - 96 + duration_offset
        clock += 1
    return clock - 1

# My input
with open("d7.txt", "r") as f:
    data = "".join(f.readlines())
    data = data.rstrip("\n")

# Part 1
# Test cases
test_input = "Step C must be finished before step A can begin.\nStep C must be finished before step F can begin.\nStep A must be finished before step B can begin.\nStep A must be finished before step D can begin.\nStep B must be finished before step E can begin.\nStep D must be finished before step E can begin.\nStep F must be finished before step E can begin."
print(f"Expected {'CABDFE'} and got {d7_1(test_input)}")
test_input = "Step J must be finished before step C can begin.\nStep I must be finished before step J can begin.\nStep J must be finished before step A can begin.\nStep A must be finished before step Q can begin.\nStep X must be finished before step I can begin."
print(f"Expected {'XIJACQ'} and got {d7_1(test_input)}")

res = d7_1(data)
print(f"Part 1 {res}")

# Part 2
# Test cases
test_input = "Step C must be finished before step A can begin.\nStep C must be finished before step F can begin.\nStep A must be finished before step B can begin.\nStep A must be finished before step D can begin.\nStep B must be finished before step E can begin.\nStep D must be finished before step E can begin.\nStep F must be finished before step E can begin."
print(f"Expected {15} and got {d7_2(test_input, 2, 0)}")

print(f"Part 2 {d7_2(data, 5, 60)}")
