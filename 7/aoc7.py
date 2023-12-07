from collections import Counter


with open("input.txt", "r") as file:
    lines = file.readlines()

hands = []
bids = []

for line in lines:
    line_split = line.strip().split(" ")
    hands.append(list(line_split[0].strip()))
    bids.append(int(line_split[1].strip()))


def aoc7_1():
    values = []

    def sort_by_hand(value):
        hand_order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        return tuple(hand_order.index(char) for char in value["hand"])

    for hand, bid in zip(hands, bids):
        result = Counter(hand)

        if result.most_common(1)[0][1] == 5:
            value = 7
        elif result.most_common(1)[0][1] == 4:
            value = 6
        elif result.most_common(2)[0][1] == 3 and result.most_common(2)[1][1] == 2:
            value = 5
        elif result.most_common(1)[0][1] == 3:
            value = 4
        elif result.most_common(2)[0][1] == 2 and result.most_common(2)[1][1] == 2:
            value = 3
        elif result.most_common(1)[0][1] == 2:
            value = 2
        else:
            value = 1

        values.append({"value": value, "bid": bid, "hand": hand})
    sorted_values = sorted(values, key=lambda x: (x["value"], sort_by_hand(x)))

    i = 1
    sum = 0
    for sorted_value in sorted_values:
        sum += sorted_value["bid"] * i
        i += 1

    print(sum)


def aoc7_2():
    values = []

    def sort_by_hand(value):
        hand_order = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
        return tuple(hand_order.index(char) for char in value["hand"])

    for hand, bid in zip(hands, bids):
        result = Counter(hand)

        j_count = result["J"]
        if j_count > 0 and j_count < 5:
            del result["J"]

        if result.most_common(1)[0][1] + j_count == 5 or j_count == 5:
            value = 7
        elif result.most_common(1)[0][1] + j_count == 4:
            value = 6
        elif (
            result.most_common(2)[0][1] + j_count == 3
            and result.most_common(2)[1][1] == 2
        ):
            value = 5
        elif result.most_common(1)[0][1] + j_count == 3:
            value = 4
        elif (
            result.most_common(2)[0][1] + j_count == 2
            and result.most_common(2)[1][1] == 2
        ):
            value = 3
        elif result.most_common(1)[0][1] + j_count == 2:
            value = 2
        else:
            value = 1

        values.append({"value": value, "bid": bid, "hand": hand})

    sorted_values = sorted(values, key=lambda x: (x["value"], sort_by_hand(x)))

    i = 1
    sum = 0
    for sorted_value in sorted_values:
        sum += sorted_value["bid"] * i
        i += 1

    print(sum)


aoc7_1()
aoc7_2()
