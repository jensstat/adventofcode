from collections import defaultdict

with open("data_folder/data4.txt") as file:
    dataset = [code.strip() for code in file.readlines()]

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
    
total_cards = sum(sum_cards)

print(total_cards)