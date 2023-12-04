with open("input.txt", "r") as file:
    lines = file.readlines()

array = []
for line in lines:
    array.append(list(line.strip()))


def aoc3_1():
    array = []
    total = 0
    for line in lines:
        array.append(list(line.strip()))
    for y, row in enumerate(array):
        cur_digit_str = ""
        for x, char in enumerate(row):
            if char.isdigit():
                cur_digit_str += char
            if cur_digit_str != "" and (not char.isdigit() or x == len(row) - 1):
                found = False
                last_digit_x = x if char.isdigit() else x - 1
                first_digit_x = x - len(cur_digit_str)
                loop_start_y = max(0, y - 1)
                loop_end_y = min(len(array) - 1, y + 1)
                loop_start_x = max(0, first_digit_x - 1)
                loop_end_x = min(len(row) - 1, last_digit_x + 1)
                for cy in range(loop_start_y, loop_end_y + 1):
                    for cx in range(loop_start_x, loop_end_x + 1):
                        if not array[cy][cx].isdigit() and array[cy][cx] != ".":
                            found = True
                if found:
                    total += int(cur_digit_str)
                cur_digit_str = ""
    print(total)


def aoc3_2():
    ratio_sum = 0
    for y, row in enumerate(array):
        for x, char in enumerate(row):
            if char == "*":
                gear_numbers = []
                loop_start_y = max(0, y - 1)
                loop_end_y = min(len(array) - 1, y + 1)
                loop_start_x = max(0, x - 1)
                loop_end_x = min(len(row) - 1, x + 1)

                for cy in range(loop_start_y, loop_end_y + 1):
                    cur_digit_str = ""
                    for cx in range(loop_start_x, loop_end_x + 1):
                        if array[cy][cx].isdigit():
                            if cur_digit_str != "":
                                cur_digit_str += array[cy][cx]
                            else:
                                cur_digit_str += array[cy][cx]
                                check_x = cx - 1
                                while check_x >= 0 and array[cy][check_x].isdigit():
                                    cur_digit_str = array[cy][check_x] + cur_digit_str
                                    check_x -= 1
                        if not array[cy][cx].isdigit() and cur_digit_str != "":
                            gear_numbers.append(int(cur_digit_str))
                            cur_digit_str = ""
                        if cx == loop_end_x and cur_digit_str != "":
                            check_x = cx + 1
                            while check_x < len(row) and array[cy][check_x].isdigit():
                                cur_digit_str += array[cy][check_x]
                                check_x += 1
                            gear_numbers.append(int(cur_digit_str))
                if len(gear_numbers) == 2:
                    ratio_sum += gear_numbers[0] * gear_numbers[1]
    print(ratio_sum)


aoc3_1()
aoc3_2()
