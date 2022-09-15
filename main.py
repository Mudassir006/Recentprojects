import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = 'blank_states_img.gif'

screen.addshape(image)

turtle.shape(image)
x = (pandas.read_csv('50_states.csv'))
guessed = []
while len(guessed) < 50:
    answer = screen.textinput(title=f"{len(guessed)}/50", prompt="Write the name of the states").title()
    co = x['state'].tolist()

    for c in co:
        if answer == 'Exit':
            ms = []
            for c in co:
                if c not in guessed:
                    ms.append(c)
            nd = pandas.DataFrame(ms)
            nd.to_csv("states_to_learn.csv")


            break


        if answer == c:
            guessed.append(answer)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = x[x.state == answer]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(state_data.state.item())
screen.exitonclick()
