from collections import defaultdict

with open("data_folder/data4.txt") as file:
    dataset = [code.strip() for code in file.readlines()]

dataset = [
'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
]
total_cards = 0

#preprocess
cards = [card.split(':') + [1] for card in dataset]
sum_cards = [1]*len(cards)

for count, card in enumerate(cards):
    card_list = card[1].split()
    split_index = card_list.index('|')
    card_numbers = card_list[:split_index]
    player_numbers = card_list[split_index+1:]

    #card_numbers = card[2:split_index]
    #player_numbers = card[split_index+1:]
    #winning_numbers = [x for x in player_numbers if x in card_numbers]
    
    card_numbers = set(card_list[:split_index])
    player_numbers = set(card_list[split_index + 1:])
    winning_numbers = player_numbers.intersection(card_numbers)

    for i in range(len(winning_numbers)):
        sum_cards[count+i+1] += sum_cards[count]
    
#total_cards = sum(card[2] for card in cards)
total_cards = sum(sum_cards)

print(total_cards)