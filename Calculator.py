logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""



def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def add(num1, num2):
    return num1 + num2


def calculator():
    print(logo)
    first_num = float(input("First Number?: "))
    while True:
        operation = input("+\n-\n*\n/\nEnter operation: ")
        second_num = float(input(f"{first_num} {operation} "))
        operations = {
            "+": add(first_num, second_num),
            "-": sub(first_num, second_num),
            "*": mul(first_num, second_num),
            "/": div(first_num, second_num)
        }

        print(f"{first_num} {operation} {second_num} = {operations[operation]}")
        first_num = operations[operation]
        print()
        if input(f"Type 'y' to continue with {first_num} or 'n' to start new calculation: ").lower() == "n":
            print()
            calculator()


calculator()
