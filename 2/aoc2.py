cube_count = {"red": 0, "green": 0, "blue": 0}

with open('input.txt', 'r') as file:
    lines = file.readlines()


def aoc2_1():
    total = 0
    for line in lines:
        game_split = line.split(":")
        draw_split = game_split[1].split(";")
        found = any((color.split()[1] == "red" and int(color.split()[0]) > 12) or
                    (color.split()[1] == "green" and int(color.split()[0]) > 13) or
                    (color.split()[1] == "blue" and int(color.split()[0]) > 14)
                    for draw in draw_split for color in draw.split(","))
        if not found:
            total += int(game_split[0].split()[1])
    print(total)


def aoc2_2():
    total = 0
    for line in lines:
        max_cube_count = {"red": 0, "green": 0, "blue": 0}
        game_split = line.split(":")
        draw_split = game_split[1].split(";")
        for draw in draw_split:
            for color in draw.split(","):
                color_count, color_name = color.split()
                max_cube_count[color_name] = max(max_cube_count[color_name], int(color_count))
        power = 1
        for v in max_cube_count.values():
            power *= v
        total += power
    print(total)


aoc2_1()
aoc2_2()
