from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
try:
    words_df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_df = pandas.read_csv("data/french_words.csv")
    words_dict = original_df.to_dict(orient="records")
else:
    words_dict = words_df.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def is_known():
    words_dict.remove(current_card)
    data = pandas.DataFrame(words_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
