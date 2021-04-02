import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

print("\t\t\tRock, Paper and Scissors *HARDEST*")
while True:
    print("What do you choose?")
    num = int(input("0 for rock, 1 for paper and 2 for scissors: "))
    if num > 2 or num < 0:
        print("Inavlid choice.\nYou lost")
        break
    user_choice = choices[num]
    print(user_choice)
    print("Computer chose:")
    if user_choice == rock:
        comp_choice = random.choice(choices)
        print(comp_choice)
        if comp_choice == rock:
            print("Its a draw")
        elif comp_choice == paper:
            print("You lost")
        else:
            print("You won!!")
    elif user_choice == paper:
        comp_choice = random.choice(choices)
        print(comp_choice)
        if comp_choice == rock:
            print("You won!!")
        elif comp_choice == paper:
            print("Its a draw")
        else:
            print("You lost")
    else:
        comp_choice = random.choice(choices)
        print(comp_choice)
        if comp_choice == rock:
            print("You lost")
        elif comp_choice == paper:
            print("You Won!!")
        else:
            print("Its a draw")

    cont = input("Do you want to continue playing (Y/N)").lower()
    if cont == "n":
        print("Okay Goodbye!!")
        break
    else:
        continue
