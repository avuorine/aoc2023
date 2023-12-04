def aoc1_1():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        sum = 0
        for line in lines:
            first_digit = None
            last_digit = None
            for char in line:
                if char.isdigit():
                    if first_digit is None:
                        first_digit = char
                    last_digit = char

            sum += int(str(first_digit) + str(last_digit))

        print(sum)


numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def aoc1_2():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        sum = 0
        for line in lines:
            cur_string = ""
            first_digit = None
            last_digit = None
            for char in line:        
                if char.isdigit():
                    if first_digit is None:
                        first_digit = char
                    last_digit = char
                    cur_string = ""
                else:
                    cur_string += char

                for key in numbers.keys():
                    if key in cur_string:
                        if first_digit is None:
                            first_digit = numbers[key]
                        last_digit = numbers[key]

            reversed_string = cur_string[::-1]
            reverse_digit = ""
            found = False
            for char in reversed_string:
                reverse_digit += char
                for key in numbers.keys():
                    reversed_key = key[::-1]
                    if reversed_key in reverse_digit:
                        last_digit = numbers[key]
                        found = True
                        break
                if found:
                    break

            sum += int(str(first_digit) + str(last_digit))

        print(sum)


aoc1_1()
aoc1_2()
