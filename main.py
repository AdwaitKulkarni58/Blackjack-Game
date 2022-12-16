############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

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
    
    if (sum_of_user_cards == 0 or sum_of_computer_cards == 0 or sum_of_user_cards > 21):
        is_game_over = True
    else:
        user_input = input("Do you want to draw another card? (y/n): ")
        if user_input == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
