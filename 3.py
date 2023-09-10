import turtle
import pandas

print_turtle = turtle.Turtle()
print_turtle.hideturtle()
print_turtle.penup()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []


while len(all_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 State Correct",
                                    prompt="what's another state").title()
    if answer_state == "Exit":
        need_to_learn = []
        for state in all_states:
            if state not in guessed_state:
                need_to_learn.append(state)
        data = pandas.DataFrame(need_to_learn)
        data.to_csv("American_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        state_data = data[data.state == answer_state]
        print_turtle.goto(int(state_data.x), int(state_data.y))
        print_turtle.write(answer_state)


# data_dict = {
#     "Fur color" : ["Gray", "Red", "Black"],
#     "Count" : [gray_count, red_count, black_count]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("squirrel_count.csv")
