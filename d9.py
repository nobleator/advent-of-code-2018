class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class LinkedList:
    def __init__(self, starting_node_value):
        self.current = Node(starting_node_value)
        self.current.left = self.current
        self.current.right = self.current

    def __repr__(self):
        out = [self.current.value]
        head = self.current.right
        while head != self.current:
            out.append(head.value)
            head = head.right
        return str(out)
    
    def add_node(self, node_value):
        # This addition method actually inserts 2 spots away from the current node
        offset_node = self.current.right
        new_node = Node(node_value)
        new_node.left = offset_node
        new_node.right = offset_node.right
        offset_node.right.left = new_node
        offset_node.right = new_node
        self.current = new_node
    
    def remove_node(self):
        # Removes and returns value of node 7 spaces to left of current
        pointer = self.current
        for _ in range(7):
            pointer = pointer.left
        retval = pointer.value
        left = pointer.left
        right = pointer.right
        left.right = right
        right.left = left
        self.current = right
        return retval


def d9_1(data):
    # Brute force implementation, works for part 1, too slow for part 2
    data = data.split(" ")
    num_players = int(data[0])
    last_marble = int(data[6])
    circle = [0]
    current_indx = 0
    current_player = 1
    scores = {p: 0 for p in range(1, num_players + 1)}
    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            scores[current_player] += marble
            for _ in range(7):
                current_indx -= 1
                if current_indx < 0:
                    current_indx = len(circle) - 1
            # Popping from the list inherently shifts the current index to the proper spot
            scores[current_player] += circle.pop(current_indx)
            if current_indx > len(circle):
                current_indx = 0
        else:
            # If current index is greater than the circle then it will just append, which is fine
            current_indx += 1
            if current_indx >= len(circle):
                current_indx = 0
            current_indx += 1
            circle.insert(current_indx, marble)
        current_player += 1
        if current_player > max(scores):
            current_player = 1
    return max(scores.values())

def d9_2(data, multiplier):
    data = data.split(" ")
    num_players = int(data[0])
    last_marble = int(data[6])
    last_marble = last_marble * multiplier
    scores = {p: 0 for p in range(num_players)}
    circle = LinkedList(0)
    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            to_add = circle.remove_node()   
            scores[(marble - 1) % num_players] += marble + to_add
        else:
            circle.add_node(marble)
    return max(scores.values())

# My input
with open("d9.txt", "r") as f:
    data = "".join(f.readlines())
    data = data.rstrip("\n")

# Part 1
# Test cases
test_input = "9 players; last marble is worth 25 points"
print(f"Expected {32} and got {d9_1(test_input)}")
test_input = "10 players; last marble is worth 1618 points"
print(f"Expected {8317} and got {d9_1(test_input)}")
test_input = "13 players; last marble is worth 7999 points"
print(f"Expected {146373} and got {d9_1(test_input)}")
test_input = "17 players; last marble is worth 1104 points"
print(f"Expected {2764} and got {d9_1(test_input)}")
test_input = "21 players; last marble is worth 6111 points"
print(f"Expected {54718} and got {d9_1(test_input)}")
test_input = "30 players; last marble is worth 5807 points"
print(f"Expected {37305} and got {d9_1(test_input)}")

res = d9_1(data)
print(f"Part 1 {res}")

# Part 2
# Test cases
test_input = "9 players; last marble is worth 25 points"
print(f"Expected {32} and got {d9_2(test_input, 1)}")
test_input = "1 players; last marble is worth 47 points"
print(f"Expected {95} and got {d9_2(test_input, 1)}")
test_input = "10 players; last marble is worth 1618 points"
print(f"Expected {8317} and got {d9_2(test_input, 1)}")
test_input = "13 players; last marble is worth 7999 points"
print(f"Expected {146373} and got {d9_2(test_input, 1)}")
test_input = "17 players; last marble is worth 1104 points"
print(f"Expected {2764} and got {d9_2(test_input, 1)}")
test_input = "21 players; last marble is worth 6111 points"
print(f"Expected {54718} and got {d9_2(test_input, 1)}")
test_input = "30 players; last marble is worth 5807 points"
print(f"Expected {37305} and got {d9_2(test_input, 1)}")

print(f"Part 2 {d9_2(data, 100)}")
