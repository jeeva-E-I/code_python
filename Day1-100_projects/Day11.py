#BlackJack Program
import os
import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
def blackjack():
    print(logo)
    def card_selection():
        '''Returns the card_value'''
        cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
        card = random.choice(cards)
        return card
    user_card = []
    comp_card = []
    is_game_over = False

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) ==2: # check if user and comp have value of 21 
            return 0
        if 11 in cards and sum(cards) > 21: # if 11 in card value and sum of the card value is greater than 21 means change 11 as 1
            cards.remove(11)
            cards.append(1)
        return sum(cards)
    def compare_result(user_score,comp_score):
        ''' compare user and computer score and return the result'''
        if user_score == comp_score:
            return "Draw"
        elif comp_score == 0:
            return "You lose"
        elif user_score == 0:
            return "You won"
        elif user_score > 21:
            return "You score is high.....You lose"
        elif comp_score > 21:
            return "Opponent score is high....... You win"
        elif user_score > comp_score:
            return "You won"
        else:
            return "You lose"
        
            
    for _ in range(2): # Triggering the card_selection function to get values for user and computer card
        user_card.append(card_selection())
        comp_card.append(card_selection())
    while not is_game_over:
        user_score = calculate_score(user_card)
        comp_score = calculate_score(comp_card)
        print(f"Your card : {user_card} - current score: {user_score}")
        print(f"Computer first card : {comp_card[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            check = input("Type 'yes' to get another card, type 'n' to pass: ").lower()
            if check == 'yes':
                user_card.append(card_selection())
            else:
                is_game_over = True
    while comp_score != 0 and comp_score < 17:   # for computer
        comp_card.append(card_selection())
        comp_score = calculate_score(comp_card)

    print(compare_result(user_score,comp_score))
    
restart = input("Do you want to play again: type 'yes' to continue and type 'no' to exit: ").lower()
if restart == 'yes':
    clear()
    blackjack()
else:
    exit()