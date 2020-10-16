#!/usr/bin/env python3

from tkinter import *
import tkinter.font as tkFont

def main():
    top = Tk()
    top.title("BSC text editor")

    # text field
    uni = tkFont.Font(family="Courier")
    field = Text(top, height=20, font=uni)
    field.pack(side=TOP)

    # current address and char
    botDisplay = Frame(top)
    botDisplay.pack(side=BOTTOM)

    # declaring elements
    addressLabel = Label(botDisplay, text="current address: ")
    addressDisp = Text(botDisplay, height=1, width=10)

    charLabel = Label(botDisplay, text="current char: ")
    charDisp = Text(botDisplay, height=1, width=10)

    # packing elements in order
    addressLabel.pack(side=LEFT)
    addressDisp.pack(side=LEFT)

    charDisp.pack(side=RIGHT)
    charLabel.pack(side=RIGHT)

    top.mainloop()

if __name__ == "__main__":
    main()