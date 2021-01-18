print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("left or right?")
answer = input().lower()
if answer == "left":
    print("There is a lake!")
    ans = input("Would you like to wait for a boat or swim across?(type swim or wait): ").lower()
    if ans == "wait":
        print("Okay...")
        print("Now you are in front of three doors Red, Blue and Yellow")
        ans_door = input("Which door do you choose to open? (red, blue or yellow): ")
        if ans_door == "yellow":
            print("Voila!! you win.")
        elif ans_door == "blue":
            print("Eaten by beasts")
            print("GAME OVER")
        elif ans_door == "red":
            print("Burned by fire")
            print("GAME OVER")
        else:
            print("GAME OVER")
    else:
        print("Attacked by trout")
        print("GAME OVER")
else:
    print("You fell into hole")
    print("GAME OVER")signa