import math


with open("input.txt", "r") as file:
    lines = file.readlines()

times = [int(num) for num in lines[0].strip().split(":")[1].strip().split(" ") if num]
distances = [
    int(num) for num in lines[1].strip().split(":")[1].strip().split(" ") if num
]

results = []


def aoc6_1():
    wins = []
    for time_idx in range(len(times)):
        race = []
        wins_in_race = 0
        for i in range(times[time_idx]):
            speed = 1 * i
            time_left = times[time_idx] - i
            distance = speed * time_left
            if distance > distances[time_idx]:
                wins_in_race += 1
            race.append(distance)
        wins.append(wins_in_race)
    product = math.prod(wins)
    print(product)


def aoc6_2():
    race_time = int("".join(str(time) for time in times))
    race_distance = int("".join(str(distance) for distance in distances))
    wins_in_race = 0
    for i in range(race_time):
        speed = 1 * i
        time_left = race_time - i
        distance = speed * time_left
        if distance > race_distance:
            wins_in_race += 1
    print(wins_in_race)


aoc6_1()
aoc6_2()
