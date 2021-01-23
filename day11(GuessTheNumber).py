import random
logo = '''

 +-+-+-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+
 |W|e|l|c|o|m|e| |t|o| |t|h|e| |N|u|m|b|e|r| |G|u|e|s|s|i|n|g| |G|a|m|e|
 +-+-+-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+


'''

ans = random.randint(1, 101)
win = False
print("\t\t", logo)
print("I'm thinking of a number between 1 and 100.")
easy_or_hard = input("Choose a difficulty. Type easy or hard: ")


def easy():
    '''This modules is for easy difficulty of the game.
    It gives user 10 total guesses to guess the number.'''
    guesses = 10
    while guesses >= 1:
        print(f"You have {guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guesses == 1:
            if guess < ans:
                if ans - guess > 6:
                    print("Too low.")
                else:
                    print("Close but still low.")
            elif guess > ans:
                if guess - ans > 6:
                    print("Too high.")
                else:
                    print("Close but still high.")
        elif guess < ans:
            if ans - guess > 6:
                print("Too low.")
                print("Guess again")
            else:
                print("Close but still low.")
                print("Guess again.")
        elif guess > ans:
            if guess - ans > 6:
                print("Too high.")
                print("Guess again")
            else:
                print("Close but still high.")
                print("Guess again.")
        else:
            global win
            win = True
            break
        guesses -= 1


def hard():
    '''This modules is for hard difficulty of the game.
    It gives user 5 total guesses to guess the number.'''
    guesses = 5
    while guesses > 0:
        print(f"You have {guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guesses == 1:
            if guess < ans:
                if ans - guess > 6:
                    print("Too low.")
                else:
                    print("Close but still low.")
            elif guess > ans:
                if guess - ans > 6:
                    print("Too high.")
                else:
                    print("Close but still high.")
        elif guess < ans:
            if ans - guess > 6:
                print("Too low.")
                print("Guess again")
            else:
                print("Close but still low.")
                print("Guess again.")

        elif guess > ans:
            if guess - ans > 6:
                print("Too high.")
                print("Guess again")
            else:
                print("Close but still high.")
                print("Guess again.")

        else:
            global win
            win = True
            break
        guesses -= 1

if easy_or_hard == "easy":
    easy()
else:
    hard()

if win:
    print(f"You got it! The answer was {ans}.")
else:
    print(f"All attempts are over. You lost, the right answer was {ans}.")