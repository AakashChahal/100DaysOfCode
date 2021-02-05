import turtle
import pandas as pd
TOTAL = 50
guessed = []
screen = turtle.Screen()
screen.title("India states game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
states_data = pd.read_csv("50_states.csv")
states = states_data.state.to_list()
# def get_mouse_coor(x, y):
#     print(x, y)
#
#
# turtle.onclick(get_mouse_coor)
while len(guessed) != TOTAL:
    ans_state = screen.textinput(title=f"{len(guessed)}/{TOTAL}Guess State", prompt="Enter a state name: ").title()
    if ans_state == "Exit":
        missing_state = [state for state in states if state not in guessed]
        for state in missing_state:
            t = turtle.Turtle()
            t.ht()
            t.penup()
            t.speed(10)
            state_pos = states_data[states_data.state == state]
            t.setpos(int(state_pos.x), int(state_pos.y))
            t.write(state)
        break
    if ans_state in states:
        t = turtle.Turtle()
        t.penup()
        t.ht()
        state = states_data[states_data.state == ans_state]
        t.setpos(int(state.x), int(state.y))
        t.write(ans_state)
        guessed.append(ans_state)


turtle.mainloop()
