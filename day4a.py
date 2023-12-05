from collections import defaultdict

with open("data_folder/data4.txt") as file:
    dataset = [code.strip() for code in file.readlines()]

cards = [card.split(':') + [1] for card in dataset]

points = 0
for count, card in enumerate(cards):
    card_list = card[1].split()
    split_index = card_list.index('|')
    """
    card_numbers = card[2:split_index]
    player_numbers = card[split_index+1:]
    winning_numbers = [x for x in player_numbers if x in card_numbers]
    """
    card_numbers = set(card_list[:split_index])
    player_numbers = set(card_list[split_index + 1:])
    winning_numbers = player_numbers.intersection(card_numbers)
    
    if len(winning_numbers)>0:
        points += 2**(len(winning_numbers)-1)

print(points)