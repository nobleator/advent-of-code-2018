import datetime


def d4_1(data):
    data = data.split("\n")
    events = {}
    # asleep_minutes = {guard_id: {minute: num_times_asleep}}
    asleep_minutes = {}
    for row in data:
        row = row.lstrip("[")
        timestamp, event = row.split("] ")
        events[datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M")] = event
    fell_asleep_at = None
    guard_id = None
    for timestamp in sorted(events):
        event = events[timestamp]
        if "#" in event:
            guard_id = int(event.lstrip("Guard #").split(" ")[0])
            if guard_id not in asleep_minutes:
                asleep_minutes[guard_id] = {}
            fell_asleep_at = None
        if "asleep" in event:
            fell_asleep_at = timestamp
        if "wakes" in event:
            for minute in range(fell_asleep_at.minute, timestamp.minute):
                if minute not in asleep_minutes[guard_id]:
                    asleep_minutes[guard_id][minute] = 1
                else:
                    asleep_minutes[guard_id][minute] += 1
    sleepiest_guard = max(asleep_minutes, key=lambda g: sum(asleep_minutes[g].values()))
    sleepiest_minute = max(asleep_minutes[sleepiest_guard], key=lambda m: asleep_minutes[sleepiest_guard][m])
    return sleepiest_guard * sleepiest_minute

def d4_2(data):
    data = data.split("\n")
    events = {}
    # asleep_minutes = {guard_id: {minute: num_times_asleep}}
    asleep_minutes = {}
    for row in data:
        row = row.lstrip("[")
        timestamp, event = row.split("] ")
        events[datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M")] = event
    fell_asleep_at = None
    guard_id = None
    for timestamp in sorted(events):
        event = events[timestamp]
        if "#" in event:
            guard_id = int(event.lstrip("Guard #").split(" ")[0])
            if guard_id not in asleep_minutes:
                asleep_minutes[guard_id] = {}
            fell_asleep_at = None
        if "asleep" in event:
            fell_asleep_at = timestamp
        if "wakes" in event:
            for minute in range(fell_asleep_at.minute, timestamp.minute):
                if minute not in asleep_minutes[guard_id]:
                    asleep_minutes[guard_id][minute] = 1
                else:
                    asleep_minutes[guard_id][minute] += 1
    sleepiest_guard = 0
    sleepiest_minute = 0
    max_occurances = 0
    for guard in asleep_minutes:
        for minute in asleep_minutes[guard]:
            if asleep_minutes[guard][minute] > max_occurances:
                sleepiest_guard = guard
                sleepiest_minute = minute
                max_occurances = asleep_minutes[guard][minute]
    return sleepiest_guard * sleepiest_minute

# My input
with open("d4.txt", "r") as f:
    data = "".join(f.readlines())
    data = data.rstrip("\n")

# Part 1
# Test cases
test_input = "[1518-11-01 00:00] Guard #10 begins shift\n[1518-11-01 00:05] falls asleep\n[1518-11-01 00:25] wakes up\n[1518-11-01 00:30] falls asleep\n[1518-11-01 00:55] wakes up\n[1518-11-01 23:58] Guard #99 begins shift\n[1518-11-02 00:40] falls asleep\n[1518-11-02 00:50] wakes up\n[1518-11-03 00:05] Guard #10 begins shift\n[1518-11-03 00:24] falls asleep\n[1518-11-03 00:29] wakes up\n[1518-11-04 00:02] Guard #99 begins shift\n[1518-11-04 00:36] falls asleep\n[1518-11-04 00:46] wakes up\n[1518-11-05 00:03] Guard #99 begins shift\n[1518-11-05 00:45] falls asleep\n[1518-11-05 00:55] wakes up"
print(f"Expected {240} and got {d4_1(test_input)}")

res = d4_1(data)
print(f"Part 1 {res}")

# Part 2
# Test cases
test_input = "[1518-11-01 00:00] Guard #10 begins shift\n[1518-11-01 00:05] falls asleep\n[1518-11-01 00:25] wakes up\n[1518-11-01 00:30] falls asleep\n[1518-11-01 00:55] wakes up\n[1518-11-01 23:58] Guard #99 begins shift\n[1518-11-02 00:40] falls asleep\n[1518-11-02 00:50] wakes up\n[1518-11-03 00:05] Guard #10 begins shift\n[1518-11-03 00:24] falls asleep\n[1518-11-03 00:29] wakes up\n[1518-11-04 00:02] Guard #99 begins shift\n[1518-11-04 00:36] falls asleep\n[1518-11-04 00:46] wakes up\n[1518-11-05 00:03] Guard #99 begins shift\n[1518-11-05 00:45] falls asleep\n[1518-11-05 00:55] wakes up"
print(f"Expected {4455} and got {d4_2(test_input)}")

print(f"Part 2 {d4_2(data)}")

