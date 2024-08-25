from tkinter import *
import random

root = Tk()
root.geometry("300x300")
root.title("🅁🄾🄲🄺 🄿🄰🄿🄴🅁 🅂🄲🄸🅂🅂🄾🅁")
comp_value ={"0":"rock","1":"paper","2":"scissor"}

def reset_game():
    b1["state"]="active"
    b2["state"]="active"
    b3["state"]="active"
    l1.config(text = "player")
    l3.config(text = "compter")
    l4.config(text =" ")

def disable_button():
    b1["state"]="disable"
    b2["state"]="disable"
    b3["state"]="disable"

def isrock():
    c_v = comp_value[str(random.randint(0,2))]
    if c_v == "rock":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        match_result = "Player win"
    else:
        match_result = "Computer win"
    l4.config(text = match_result)
    l1.config(text = "Rock      ")
    l3.config(text = c_v)
    disable_button()

def ispaper():
    c_v = comp_value[str(random.randint(0,2))]
    if c_v == "paper":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        match_result = "computer win"
    else:
        match_result = "player win"
    l4.config(text = match_result)
    l1.config(text = "Paper      ")
    l3.config(text = c_v)
    disable_button()

def isscissor():
    c_v = comp_value[str(random.randint(0,2))]
    if c_v == "rock":
        match_result = "computer Draw"
    elif c_v == "Scissor":
        match_result = "match draw"
    else:
        match_result = "player win"
    l4.config(text = match_result)
    l1.config(text = "scisssor      ")
    l3.config(text = c_v)
    disable_button()

Label(root, text="R̳o̳c̳k̳ p̳a̳p̳e̳r̳ s̳c̳i̳s̳s̳o̳r̳", font ="normal 20 bold", fg="cyan").pack(pady=20)
frame = Frame(root)
frame.pack()

l1 = Label(frame,text="PLAYER", font=10)
l2 = Label(frame,text="Vs", font="normal 20 bold")
l3 = Label(frame,text="COMPUTER", font=10)

l1.pack(side= LEFT)
l2.pack(side= LEFT)
l3.pack(side= RIGHT)

l4 = Label(root,text="",font="normal 20 bold", bg="white",width=15,borderwidth=2,relief="solid")
l4.pack(pady=20)

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text="Rock⛰", font=10, width=7,bg="grey", command=isrock)
b2 = Button(frame1, text="Paper📃", font=10, width=7,bg="white", command=ispaper)
b3 = Button(frame1, text="Scissor✂", font=10, width=7,bg="red", command=isscissor)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

Button(root, text="Play again",font=10, fg="red",bg="black", command=reset_game).pack(pady=20)

root.mainloop()


























