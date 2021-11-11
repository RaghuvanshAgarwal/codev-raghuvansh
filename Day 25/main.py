import turtle
import pandas
from text import Text

IMAGE = "blank_states_img.gif"
STATES_TO_LEARN_FILE_PATH = "states_to_learn.csv"
STATES_DATA = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S States")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

open_states_list = STATES_DATA["state"].to_list()
closed_states_list = []
should_continue = True

while should_continue:
    user_input = screen.textinput(title=f"{len(closed_states_list)} /" +
                                        f"{len(open_states_list) + len(closed_states_list)} States", prompt="What's "
                                                                                                            "Another "
                                                                                                            "State "
                                                                                                            "Name? | "
                                                                                                            "'exit' "
                                                                                                            "for Exit")
    if user_input:
        user_input = user_input.title()
        if user_input in open_states_list:
            state = STATES_DATA[STATES_DATA["state"] == user_input]
            Text((int(state.x), int(state.y)), user_input)
            open_states_list.remove(user_input)
            closed_states_list.append(user_input)
        should_continue = len(open_states_list) > 0 and user_input != "Exit"
        if user_input == "Exit":
            screen.bye()
            should_continue = False

missed_states = {"Missed States": open_states_list}
pandas.DataFrame(missed_states).to_csv(STATES_TO_LEARN_FILE_PATH)
