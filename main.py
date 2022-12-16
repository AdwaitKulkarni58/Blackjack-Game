############### Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    random_number = random.randrange(len(cards))
    return cards[random_number]

user_cards = []
computer_cards = []

first_user_card = deal_card()
second_user_card = deal_card()

first_computer_card = deal_card()
second_computer_card = deal_card()

user_cards.append(first_user_card)
user_cards.append(second_user_card)

user_cards.append(first_computer_card)
user_cards.append(second_computer_card)


def calculate_score(cards):
    if (sum(cards) == 21 and len(cards) == 2):
        return 0
    if (11 in cards and sum(cards) > 21):
        cards.remove(11)
        cards.append(1)
    return sum(cards)


is_game_over = False

while not is_game_over:
    sum_of_user_cards = calculate_score(user_cards)
    sum_of_computer_cards = calculate_score(computer_cards)
    
    print(f"Your cards are: {user_cards}, your score is {sum_of_user_cards}")
    print(f"The computer cards are: {computer_cards}, computer's score is {sum_of_computer_cards}")
    
    if (sum_of_user_cards == 0 or sum_of_computer_cards == 0 or sum_of_user_cards > 21):
        is_game_over = True
    else:
        user_input = input("Do you want to draw another card? (y/n): ")
        if user_input == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

while sum_of_computer_cards < 17:
    computer_cards.append(deal_card())
    sum_of_computer_cards = calculate_score(computer_cards)

def compare(sum_of_user_cards, sum_of_computer_cards):
    if sum_of_user_cards == sum_of_computer_cards:
        return "It is a draw"
    elif sum_of_computer_cards == 0:
        return "You lose"
    elif sum_of_user_cards == 0:
        return "You win"
    elif sum_of_user_cards > 21:
        return "You lose"
    elif sum_of_computer_cards > 21:
        return "You win"
    elif sum_of_user_cards > sum_of_computer_cards:
        return "You win"
    else:
        return "You lose"        

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
