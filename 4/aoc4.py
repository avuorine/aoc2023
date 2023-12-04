with open('input.txt', 'r') as file:
    lines = file.readlines()


def aoc4_1():
    total = 0
    for line in lines:
        card_id_split = line.strip().split(":")
        card = card_id_split[1].split("|")

        numbers = [int(num) for num in card[0].split(" ") if num]
        results = [int(num) for num in card[1].split(" ") if num]

        points = 0
        for number in numbers:
            for result in results:
                if number == result:
                    if (points == 0):
                        points = 1
                    else:
                        points = points * 2
        total += points
    print(total)


def aoc4_2():
    cards = []
    for line in lines:
        card_id_split = line.strip().split(":")
        card = card_id_split[1].split("|")

        numbers = [int(num) for num in card[0].split(" ") if num]
        results = [int(num) for num in card[1].split(" ") if num]

        cards.append({"numbers": numbers, "results": results})

    total_cards = [1 for _ in range(len(cards))]

    idx = 0
    for card in cards:
        pts = 0
        for number in card["numbers"]:
            for result in card["results"]:
                if number == result:
                    pts += 1

        last_card_idx_to_add = pts + idx
        for i in range(idx + 1, last_card_idx_to_add + 1):
            if i >= len(total_cards):
                break
            else:
                total_cards[i] += total_cards[idx]
        idx += 1

    print(sum(total_cards))


aoc4_1()
aoc4_2()
