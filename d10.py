import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import time


def d10_1(data):
    data = data.split("\n")
    points = []
    velocities = []
    for row in data:
        point, velocity = row.lstrip("position=<").rstrip(">").split("> velocity=<")
        # print(point, velocity)
        point = [int(e) for e in point.split(",")]
        points.append(point)
        velocity = [int(e) for e in velocity.split(",")]
        velocities.append(velocity)
    
    # Find time that has the smallest bounding box and visualize that
    smallest_diff_x = max(p[0] for p in points) - min(p[0] for p in points)
    tightest_t = 0
    for t in range(100000):
        new_points = [(points[i][0] + velocities[i][0] * t,
                       points[i][1] + velocities[i][1] * t) for i in range(len(points))]
        diff_x = max(p[0] for p in new_points) - min(p[0] for p in new_points)
        if diff_x < smallest_diff_x:
            smallest_diff_x = diff_x
            tightest_t = t
    print(smallest_diff_x, tightest_t)

    fig = plt.figure()
    new_points = [(points[i][0] + velocities[i][0] * tightest_t,
                   points[i][1] + velocities[i][1] * tightest_t) for i in range(len(points))]
    plt.scatter([p[0] for p in new_points], [p[1] for p in new_points])
    plt.show()

    # Appears upside down, correct answer is "FBHKLEAG"

    return None

def d10_2(data):
    data = data.split("\n")
    return None

# My input
with open("d10.txt", "r") as f:
    data = "".join(f.readlines())
    data = data.rstrip("\n")

# Part 1
# Test cases
# test_input = "position=< 9,  1> velocity=< 0,  2>\nposition=< 7,  0> velocity=<-1,  0>\nposition=< 3, -2> velocity=<-1,  1>\nposition=< 6, 10> velocity=<-2, -1>\nposition=< 2, -4> velocity=< 2,  2>\nposition=<-6, 10> velocity=< 2, -2>\nposition=< 1,  8> velocity=< 1, -1>\nposition=< 1,  7> velocity=< 1,  0>\nposition=<-3, 11> velocity=< 1, -2>\nposition=< 7,  6> velocity=<-1, -1>\nposition=<-2,  3> velocity=< 1,  0>\nposition=<-4,  3> velocity=< 2,  0>\nposition=<10, -3> velocity=<-1,  1>\nposition=< 5, 11> velocity=< 1, -2>\nposition=< 4,  7> velocity=< 0, -1>\nposition=< 8, -2> velocity=< 0,  1>\nposition=<15,  0> velocity=<-2,  0>\nposition=< 1,  6> velocity=< 1,  0>\nposition=< 8,  9> velocity=< 0, -1>\nposition=< 3,  3> velocity=<-1,  1>\nposition=< 0,  5> velocity=< 0, -1>\nposition=<-2,  2> velocity=< 2,  0>\nposition=< 5, -2> velocity=< 1,  2>\nposition=< 1,  4> velocity=< 2,  1>\nposition=<-2,  7> velocity=< 2, -2>\nposition=< 3,  6> velocity=<-1, -1>\nposition=< 5,  0> velocity=< 1,  0>\nposition=<-6,  0> velocity=< 2,  0>\nposition=< 5,  9> velocity=< 1, -2>\nposition=<14,  7> velocity=<-2,  0>\nposition=<-3,  6> velocity=< 2, -1>"
# print(f"Expected {'HI'} and got {d10_1(test_input)}")

res = d10_1(data)
print(f"Part 1 {res}")

# Part 2
# Test cases
# test_input = "9 players; last marble is worth 25 points"
# print(f"Expected {32} and got {d10_2(test_input, 1)}")

# print(f"Part 2 {d10_2(data, 100)}")
