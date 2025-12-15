import art
import game_data
import random

def user_choice():
    if game_data.data[user_a]['follower_count'] > game_data.data[user_b]['follower_count']:
        return "A"
    else:
        return "B"

print(art.logo)
score = 0
continue_game = True
user_b = random.randint(0, 51)
while continue_game:
    user_a = user_b
    user_b = random.randint(0, 51)
    if user_a == user_b:
        user_b = random.randint(0, 51)
    print(f"Compare A {game_data.data[user_a]['name']}, a {game_data.data[user_a]['description']} from {game_data.data[user_a]['country']}.")
    print(art.vs)
    print(f"Against B {game_data.data[user_b]['name']}, a {game_data.data[user_b]['description']} from {game_data.data[user_b]['country']}.")
    decision = input("Who has more followers? A or B").upper()
    if user_choice() == decision:
        score += 1
        print(f"Your right! Current score is {score}")
    else:
        print(f"That was wrong. Your score is {score}")
        continue_game = False




