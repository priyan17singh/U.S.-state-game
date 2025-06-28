import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. State Game.")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = list(data.state)

gussed_states = set()

while len(gussed_states) < 50:

    answer_state = turtle.textinput(title=f"{len(gussed_states)}/50 state correct", prompt="What's another state name").title()
# player wants to exit the game.
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in gussed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv") #The states you have missed.
        break

# If answer state is one of the states in 50_states.csv.
    if answer_state in all_states:
        state_data = data[data.state == answer_state]
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(arg=answer_state, align="center", font=("Arial", 8, "normal"))
        gussed_states.add(answer_state)
