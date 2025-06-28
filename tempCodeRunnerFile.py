    answer_state = turtle.textinput(title="Guess the state", prompt="What's another state name").title()

    # If answer state is one of the states in 50_states.csv.
    if answer_state in all_states:
        x = data.x[data.state == answer_state]
        y = data.y[data.state == answer_state]
        print(x)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(x),int(y))
        t.write(arg=answer_state, align="center", font=("Arial", 8, "normal"))