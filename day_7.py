# Advent of Code 2023
# Day 7: Camel Cards

from copy import deepcopy
from functools import cmp_to_key

special_cards = {
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

hands_part_1 = []

with open("inputs/day_7.txt") as file:
    for line in file:
        halves = line.split(" ")
        hands_part_1.append({
            "cards": [
                int(card) if card in "123456789" else special_cards[card]
                for card in halves[0]
            ],
            "bid": int(halves[1])
        })

hands_part_2 = deepcopy(hands_part_1)

for hand in hands_part_2:
    hand["cards"] = [0 if card == 11 else card for card in hand["cards"]]

def find_type(cards):
    set_ = set(cards)
    unique_cards = len(set_)

    if unique_cards == 1:
        return 0
    elif unique_cards == 2:
        if cards.count(cards[0]) in (1, 4):
            return 1
        else:
            return 2
    elif unique_cards == 3:
        if any(cards.count(card) == 3 for card in set_):
            return 3
        elif any(cards.count(card) == 2 for card in set_):
            return 4
    elif unique_cards == 4:
        return 5
    else:
        return 6

for hand in hands_part_1:
    hand["type"] = find_type(hand["cards"])

for hand in hands_part_2:
    if 0 in hand["cards"]:
        hand["type"] = None

        for new_card in range(15):
            if new_card != 0:
                modified_cards = [
                    new_card if card == 0 else card for card in hand["cards"]
                ]

                type_ = find_type(modified_cards)

                if hand["type"] is None or type_ < hand["type"]:
                    hand["type"] = type_
    else:
        hand["type"] = find_type(hand["cards"])

def compare_hands(hand_1, hand_2):
    if hand_1["type"] < hand_2["type"]:
        return 1
    elif hand_2["type"] < hand_1["type"]:
        return -1
    else:
        for card_1, card_2 in zip(hand_1["cards"], hand_2["cards"]):
            if card_1 > card_2:
                return 1
            elif card_2 > card_1:
                return -1

        return 0

key = cmp_to_key(compare_hands)
hands_part_1.sort(key=key)
hands_part_2.sort(key=key)

print(f"""Part 1: {
    sum(hand['bid'] * (i + 1) for i, hand in enumerate(hands_part_1))
}""")

print(f"""Part 2: {
    sum(hand['bid'] * (i + 1) for i, hand in enumerate(hands_part_2))
}""")
