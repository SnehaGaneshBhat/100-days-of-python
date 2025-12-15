import random
import art

def check_condition(gue, num):
    if gue > num:
        print("Guess lower")
    elif gue < num:
        print("Guess higher")
    elif  gue == num:
        print("You guessed the correct number. You win!!!")


def check_level(level):
    if level == "easy":
        return 10
    else:
        return 5


def play_game():
    print(art.logo)
    level = input("Enter the level. Easy or difficult.").lower()
    lives = check_level(level)
    number = random.randint(1, 100)
    while lives > 0:
        guess = int(input("Enter your guess"))
        check_condition(gue=guess, num=number)
        if guess == number:
            break
        lives -= 1
        print(f"You have {lives} lives left")
    if guess != number:
        print(f"Youve run out of guesses. the number was {number}")



play_game()








