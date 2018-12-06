def dist(p1, p2):
    # p1 and p2 should be tuples of x, y coordinates
    # Returns Manhattan distance
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def d6_1(data):
    data = data.split("\n")
    max_x = 0
    max_y = 0
    areas = {}
    points = []
    for row in data:
        (x, y) = [int(e) for e in row.split(", ")]
        points.append((x, y))
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    infinite_points = set()
    areas = {}
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            # List of tuples with (distance, point), sorted by distance
            distances = sorted([(dist(p, (x, y)), p) for p in points], key=lambda t: t[0])
            min_distance, closest_point = distances[0]
            # Make sure the minimum is unique
            if min_distance == distances[1][0]:
                continue
            # If the x or y coordinate is on the edge, then the closest point is actually an infinite point
            if x in (0, max_x) or y in (0, max_y):
                infinite_points.add(closest_point)
            if closest_point not in infinite_points:
                if closest_point in areas:
                    areas[closest_point] += 1
                else:
                    areas[closest_point] = 1
    return max(areas.values())

def d6_2(data, threshold):
    data = data.split("\n")
    max_x = 0
    max_y = 0
    points = []
    for row in data:
        (x, y) = [int(e) for e in row.split(", ")]
        points.append((x, y))
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    safe_area = 0
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if sum(dist(p, (x, y)) for p in points) < threshold:
                safe_area += 1
    return safe_area

# My input
with open("d6.txt", "r") as f:
    data = "".join(f.readlines())
    data = data.rstrip("\n")

# Part 1
# Test cases
test_input = "1, 1\n1, 6\n8, 3\n3, 4\n5, 5\n8, 9"
print(f"Expected {17} and got {d6_1(test_input)}")
test_input = "0, 0\n0, 100\n1, 50\n80, 20\n80, 50\n80, 80\n100, 0\n100, 50\n100, 100"
print(f"Expected {1876} and got {d6_1(test_input)}")

res = d6_1(data)
print(f"Part 1 {res}")

# Part 2
# Test cases
test_input = "1, 1\n1, 6\n8, 3\n3, 4\n5, 5\n8, 9"
print(f"Expected {16} and got {d6_2(test_input, 32)}")

print(f"Part 2 {d6_2(data, 10000)}")
