from tkinter import *

import pandas
import random

try:
    french_words = pandas.read_csv("words_to_learn")

except FileNotFoundError:
    french_words = pandas.read_csv('french_words.csv')
    to_dict = french_words.to_dict(orient="records")

else:
    to_dict = french_words.to_dict(orient="records")

random_word = {}


def next_card():
    global random_word, flip_timer
    windows.after_cancel(flip_timer)
    random_word = random.choice(to_dict)
    canvas.itemconfig(card_text, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_word["French"], fill="black")
    canvas.itemconfig(card_front, image=Front_image)
    windows.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_front, image=Background_image)
    canvas.itemconfig(card_text, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_word["English"], fill="white")


def is_known():
    to_dict.remove(random_word)
    data = pandas.DataFrame(to_dict)
    data.to_csv("words_to_learn")
    next_card()


# print(to_dict)

windows = Tk()
windows.title("Falsy")
windows.config(padx=20, pady=20)

flip_timer = windows.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)  ##Canvas object allows to lay lots of thing over it
Front_image = PhotoImage(file="card_front.png")
Background_image = PhotoImage(file="card_back.png")
card_front = canvas.create_image(400, 263, image=Front_image)
card_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="words", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=4)

Tick_mark_image = PhotoImage(file="right.png")
known_button = Button(image=Tick_mark_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

Cross_mark_image = PhotoImage(file="wrong.png")
unknown_button = Button(image=Cross_mark_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

next_card()

windows.mainloop()
