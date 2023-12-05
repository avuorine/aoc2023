with open("input.txt", "r") as file:
    lines = file.readlines()

seeds = []
mappings = []

i = 0
for i in range(len(lines)):
    if "seeds:" in lines[i]:
        seeds = [int(num) for num in lines[i].strip().split(":")[1].split(" ") if num]
    if ":" in lines[i] and "seeds:" not in lines[i]:
        i += 1
        mapping = []
        while i < len(lines) and lines[i] != "\n":
            mapping.append([int(num) for num in lines[i].strip().split(" ") if num])
            i += 1

        mappings.append(mapping)


def aoc5_1():
    nums = []

    for num in seeds:
        for mapping in mappings:
            for line in mapping:
                if num >= line[1] and num < line[1] + line[2]:
                    num = num + (line[0] - line[1])
                    break
        nums.append(num)

    print(min(nums))


def aoc5_2():
    nums = []
    for i in range(0, len(seeds), 2):
        for j in range(0, seeds[i + 1], 10000):
            num = seeds[i] + j
            for mapping in mappings:
                for line in mapping:
                    if num >= line[1] and num < line[1] + line[2]:
                        num = num + (line[0] - line[1])
                        break
            nums.append({seeds[i] + j: num})

    min_dict = min(nums, key=lambda dic: min(dic.values()))
    min_key = list(min_dict.keys())[0]

    nums = []
    for j in range(min_key - 10000, min_key + 10000, 1):
        num = j
        for mapping in mappings:
            for line in mapping:
                if num >= line[1] and num < line[1] + line[2]:
                    num = num + (line[0] - line[1])
                    break
        nums.append(num)

    print(min(nums))


aoc5_1()
aoc5_2()
