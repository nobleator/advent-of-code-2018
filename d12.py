def d12_1_string_approach(data):
    # Does not work, retaining for curiosity's sake
    data = data.split("\n")
    initial_state = data[0].lstrip("Initial state: ")
    notes = data[2:]
    rules = {}
    for note in notes:
        left, right = note.split(" => ")
        rules[left] = right
    plants = "." * 20 + initial_state + "." * 20
    print(initial_state)
    print(plants)
    print(rules)
    for generation in range(20):
        print(plants)
        next_gen = plants
        for i, p in enumerate(plants):
            group = plants[i - 2:i + 3]
            if group in rules:
                print("Match found!")
                print(f"Index {i}: Due to rule {group}, {p} -> {rules[group]}")
                next_gen = plants[:i] + rules[group] + plants[i + 1:]
        print(next_gen)
        plants = next_gen
    print(plants)
    return sum(i if p == "#" else 0 for i, p in enumerate(plants))


def next_gen(curr_gen, rules):
    start = min(curr_gen)
    end = max(curr_gen)
    next_gen = set()
    for indx in range(start - 3, end + 4):
        group = "".join("#" if indx + shift in curr_gen else "." for shift in [-2, -1,  0, 1, 2])
        if group in rules:
            next_gen.add(indx)
    return next_gen, rules

def d12(data):
    data = data.split("\n")
    initial_state = data[0].lstrip("initial state: ")
    rules_raw = data[2:]
    rules = set()
    for rule in rules_raw:
        left, right = rule.split(" => ")
        if right == "#":
            rules.add(left)
    state = set()
    for i, v in enumerate(initial_state):
        if v == "#":
            state.add(i)

    part_1 = -1
    part_2 = -1
    last_sum = 0
    diffs = []
    gen = 1
    while True:
        state, rules = next_gen(state, rules)
        curr_sum = sum(state)
        if gen == 20:
            part_1 = curr_sum
        diff = curr_sum - last_sum
        if gen > 20 and all(d == diff for d in diffs[-5:]):
            print(f"Last 5 diffs have been the same, gen {gen}")
            part_2 = curr_sum + ((50000000000 - gen) * diff)
            break
        diffs.append(diff)
        last_sum = curr_sum
        if gen > 10000:
            print("Reached 10000 generations")
            break
        gen += 1
    return part_1, part_2

# My input
with open("d12.txt", "r") as f:
    data = "".join(f.readlines())
    data = data.rstrip("\n")

# Parts 1 & 2
# Test cases
test_input = "initial state: #..#.#..##......###...###\n\n...## => #\n..#.. => #\n.#... => #\n.#.#. => #\n.#.## => #\n.##.. => #\n.#### => #\n#.#.# => #\n#.### => #\n##.#. => #\n##.## => #\n###.. => #\n###.# => #\n####. => #"
print(f"Expected {325} (part 2 test unknown) and got {d12(test_input)}")

print(f"Parts 1 & 2 {d12(data)}")
