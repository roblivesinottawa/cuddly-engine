import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)} / 50 States Correct",
                              prompt="What's another state's name? ").title()
    if answer == "Exit":
        missing = []
        for state in all_states:
            if state not in guessed_states:
                missing.append(state)
        new_data = pandas.DataFrame(missing)
        # generate a new file with the states not guessed
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in all_states:
        guessed_states.append(guessed_states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)






# turtle.mainloop()
# screen.exitonclick()

