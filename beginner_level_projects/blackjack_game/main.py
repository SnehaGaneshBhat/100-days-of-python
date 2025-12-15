import art
import random

def deal_cards():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    card = random.choice(cards)
    return card

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(art.logo)
    user_cards = []
    comp_cards = []
    comp_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        comp_cards.append(deal_cards())

    while not is_game_over:
        user_score = calc_score(user_cards)
        comp_score = calc_score(comp_cards)
        print(f"your cards are {user_cards} and your score is {user_score}")
        print(f"Computers first card is {comp_cards[0]}")
        if user_score == 0 or comp_score == 0 or user_score>21:
            is_game_over = True
        else:
            play_card = input("Enter 'y' to pick another card. Enter 'n' to pass: ")
            if play_card == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while comp_score !=0 and comp_score < 17:
        comp_cards.append(deal_cards())
        comp_score = calc_score(comp_cards)

    print(f"Users final hand is {user_cards} and final score is {user_score}")
    print(f"Computers final hand is {comp_cards} and final score is {comp_score}")
    print(compare(user_score, comp_score))

while input("Do you wanna play a game of Blackjack? Enter y or n") == "y":
    print("\n" * 20)
    play_game()


