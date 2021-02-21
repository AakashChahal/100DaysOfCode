import random
import os

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

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def check_cards():
    """Check if user or computer have Blackjack."""

    if 11 in comp_cards and 10 in comp_cards:
        print(f"\tYour final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"\tComputer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
        print("You Lose. Computer has a Blackjack.")
        return "lose"

    elif 11 in user_cards and 10 in user_cards:
        print(f"\tYour final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"\tComputer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
        print("You won with a Blackjack.")
        return "win"

    else:
        print(f"\tYour cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"\tComputer's first card: {comp_cards[0]}")

def scores():
    """Compares the scores of user and computers cards."""

    if sum(comp_cards) > sum(user_cards):
        print(f"\tYour final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"\tComputer's final hand {comp_cards}, final score: {sum(comp_cards)}")
        print("Opponent Win")

    elif sum(comp_cards) < sum(user_cards):
        print(f"\tYour final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"\tComputer's final hand {comp_cards}, final score: {sum(comp_cards)}")
        print("You Win")

    elif sum(comp_cards) == sum(comp_cards):
        print(f"\tYour final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"\tComputer's final hand {comp_cards}, final score: {sum(comp_cards)}")
        print("Its a draw")

def dealer():
    """Main function where all the consecutive cards after first two gets added.
    Works as a dealer."""
    check = check_cards()
    if check == "win":
        pass
    elif check == "lose":
        pass
    while True:
        next_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")
        if next_or_pass == "y":
            user_cards.append(random.choice(cards))
            if sum(user_cards) > 21:
                if 11 in user_cards:
                    user_cards.remove(11)
                    user_cards.append(1)
                    check_cards()
                else:
                    print(f"\tYour final hand: {user_cards}, final score: {sum(user_cards)}")
                    print(f"\tComputer's final hand {comp_cards}, final score: {sum(comp_cards)}")
                    print("You went over. You lose")
                    break
            else:
                check_cards()

        else:
            while sum(comp_cards) < 17:
                comp_cards.append(random.choice(cards))
            if sum(comp_cards) > 21:
                if 11 in comp_cards:
                    comp_cards.remove(11)
                    comp_cards.append(1)
                    check_cards()
                else:
                    print(f"\tYour final hand: {user_cards}, final score: {sum(user_cards)}")
                    print(f"\tComputer's final hand {comp_cards}, final score: {sum(comp_cards)}")
                    print("Opponent went over. You Win")
                    break
            else:
                scores()
                break

while True:
    user_cards = [random.choice(cards), random.choice(cards)]
    comp_cards = [random.choice(cards), random.choice(cards)]
    print(logo)
    dealer()
    if input("Do you want to play blackjack (y/n): ").lower() != "y":
        break
    os.system("cls")
