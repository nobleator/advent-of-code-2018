class Car:
    def __init__(self, x, y, delta_x, delta_y):
        self.x = x
        self.y = y
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.next_turn = "LEFT"


def viz(grid, cars=None):
    if cars == None:
        print("\n".join(["".join([char for char in row]) for row in grid]))
    else:
        all_locations = [(car.x, car.y) for car in cars]
        new_grid = []
        for row_indx, row in enumerate(grid):
            grid_row = []
            for col_indx, char in enumerate(row):
                if (col_indx, row_indx) in all_locations:
                    grid_row.append("*")
                else:
                    grid_row.append(char)
            new_grid.append(grid_row)
        print("\n".join("".join(row) for row in new_grid))


def d13(data):
    data = data.split("\n")
    cars = []
    grid = []
    for row_indx, row in enumerate(data):
        grid_row = []
        for col_indx, char in enumerate(row):
            if char in (">", "<"):
                grid_row.append("-")
                if char == ">":
                    cars.append(Car(col_indx, row_indx, 1, 0))
                else:
                    cars.append(Car(col_indx, row_indx, -1, 0))
            elif char in ("v", "^"):
                grid_row.append("|")
                if char == "v":
                    cars.append(Car(col_indx, row_indx, 0, 1))
                else:
                    cars.append(Car(col_indx, row_indx, 0, -1))
            else:
                grid_row.append(char)
        grid.append(grid_row)
    # viz(grid, cars)
    first_crash = None
    ctr = 0
    done = False
    while not done:
        # Sort by top to bottom, then left to right
        cars.sort(key=lambda x: (x.y, x.x))
        for car in cars:
            car.x += car.delta_x
            car.y += car.delta_y
            if grid[car.y][car.x] == "\\":
                temp_x = car.delta_x
                car.delta_x = car.delta_y
                car.delta_y = temp_x
            elif grid[car.y][car.x] == "/":
                temp_x = car.delta_x
                car.delta_x = -car.delta_y
                car.delta_y = -temp_x
            elif grid[car.y][car.x] == "+":
                if car.next_turn == "LEFT":
                    car.next_turn = "STRAIGHT"
                    if (car.delta_x, car.delta_y) == (0, 1) or (car.delta_x, car.delta_y) == (0, -1):
                        temp_x = car.delta_x
                        car.delta_x = car.delta_y
                        car.delta_y = temp_x
                    elif (car.delta_x, car.delta_y) == (1, 0) or (car.delta_x, car.delta_y) == (-1, 0):
                        temp_x = car.delta_x
                        car.delta_x = -car.delta_y
                        car.delta_y = -temp_x
                elif car.next_turn == "STRAIGHT":
                    car.next_turn = "RIGHT"
                elif car.next_turn == "RIGHT":
                    car.next_turn = "LEFT"
                    if (car.delta_x, car.delta_y) == (1, 0) or (car.delta_x, car.delta_y) == (-1, 0):
                        temp_x = car.delta_x
                        car.delta_x = car.delta_y
                        car.delta_y = temp_x
                    elif (car.delta_x, car.delta_y) == (0, 1) or (car.delta_x, car.delta_y) == (0, -1):
                        temp_x = car.delta_x
                        car.delta_x = -car.delta_y
                        car.delta_y = -temp_x
            all_locations = [(car.x, car.y) for car in cars]
            if len(all_locations) != len(set(all_locations)):
                crash = (car.x, car.y)
                if first_crash == None:
                    first_crash = crash
                print(f"There was a crash at {crash}!")
                cars = [c for c in cars if (c.x, c.y) != crash]
                # done = True
            if len(cars) < 2:
                if len(cars) < 1:
                    print("No cars left!!")
                    last_car = None
                    done = True
                else:
                    print("Only one car left")
                    last_car = (cars[0].x, cars[0].y)
                    done = True
        # viz(grid, cars)
    return first_crash, last_car

# My input
with open("d13.txt", "r") as f:
    data = "".join(f.readlines())
    data = data.rstrip("\n")

# Part 1
# Test cases
test_input = "/->-\\        \n|   |  /----\\\n| /-+--+-\\  |\n| | |  | v  |\n\\-+-/  \\-+--/\n  \\------/   "
print(f"Expected {7,3} and got {d13(test_input)}")

print(f"Part 1 {d13(data)}")

# Part 2
# Test cases
test_input = "/>-<\\  \n|   |  \n| /<+-\\\n| | | v\n\\>+</ |\n  |   ^\n  \\<->/"
print(f"Expected {6,4} and got {d13(test_input)}")

print(f"Part 1 {d13(data)}")
