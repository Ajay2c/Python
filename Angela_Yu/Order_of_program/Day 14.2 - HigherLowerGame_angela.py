from HigherLowerGameData import data
from art import vs, higherlower
import random


def generate_data():
    return random.choice(data)


# display the compare a


def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_count, b_count):
    if a_count == b_count:
        generate_data()
    elif a_count > b_count and guess == "a":
        return guess == "a"
    elif a_count < b_count and guess == "b":
        return guess == "b"


def game():
    score = 0

    Against_B = generate_data()
    b_follower_count = Against_B["follower_count"]
    print(b_follower_count)

    game_start = True
    while game_start:
        Compare_A = Against_B
        a_follower_count = Compare_A["follower_count"]
        print(a_follower_count)

        Against_B = generate_data()
        b_follower_count = Against_B["follower_count"]
        print(b_follower_count)

        while a_follower_count == b_follower_count:
            b_follower_count = generate_data()

        print(higherlower)
        print(f"Compare_A: {format_data(Compare_A)}")
        print(vs)
        print(f"Against_B: {format_data(Against_B)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_start = False
            print(f"Sorry, that's wrong. Final score: {score}")

        # compare the both

        # def compare


game()
