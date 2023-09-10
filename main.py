from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card= {}
to_learn= {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    o_data = pandas.read_csv("data/italiano.csv")
    to_learn = o_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Italiano", fill="black")
    canvas.itemconfig(card_word, text=current_card["Italiano"], fill="black")
    canvas.itemconfig(canvas_image, image=front_img)
    flip_timer = window.after(ms=3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(card_title, text="Inglese", fill="white")
    canvas.itemconfig(card_word, text=current_card["Inglese"], fill="white")

def known_word():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

#window
window = Tk()
window.title("Flashy")
# window.minsize(width=1000, height=800)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#flash
flip_timer = window.after(ms=3000, func=flip_card)

#charater
charater = "Bonjour"

#CardFront
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text=f"", font=("Ariel", 60, "bold"))
canvas.grid(column=0,row=0, columnspan=2)

#CardBack
back_img = PhotoImage(file="images/card_back.png")

#button right
right_img = PhotoImage(file="images/right.png")
r_button = Button(image=right_img, highlightthickness=0, command=known_word)
r_button.grid(column=1, row=1)


#button wrong
wrong_img = PhotoImage(file="images/wrong.png")
w_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
w_button.grid(column=0, row=1)



next_card()

window.mainloop()
