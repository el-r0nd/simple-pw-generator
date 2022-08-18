from tkinter import Tk, StringVar, IntVar, Label, Entry, Button, Text

from _tkinter import *
import random
import pyperclip

root = Tk()
root.geometry("300x300")
pass_str = StringVar()
pass_len=IntVar()
pass_len.set(0)


def generate_pw():
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', '!', '?', '-', '_']

    password = ""
    for i in range(pass_len.get()):
        password += random.choice(alph)
    pass_str.set(password)

def copy_clipboard():
    random_password = pass_str.get()
    pyperclip.copy(random_password)

Label(root,text="Pw Generator",font="calibri 20 bold").pack()
Label(root,text="How long password do you want?").pack(pady=2)

Entry(root,textvariable=pass_len).pack(pady=3)

Button(root,text="Generate",command=generate_pw).pack(pady=5)
Entry(root,textvariable=pass_str).pack(pady=4)
Button(root,text="Copy to clipboard",command=copy_clipboard).pack()
root.mainloop()





