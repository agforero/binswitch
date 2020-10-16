#!/usr/bin/env python3

from tkinter import *

def main():
    # initializing tkinter elements
    top = Tk()
    top.title("BSC input tool")

    # initializing current address and value as list of chars representing binary
    currentAddress = ["0" for i in range(32)]
    currentVal = ["0" for i in range(32)]

    # left side: one checkbox, toggling address/value modes
    # middle: 4 rows of 8 checkboxes = 32 checkboxes, for entry
    # right: confirmation button, sorta like an Enter key
    masterLeft = Frame(top)
    masterCenter = Frame(top)
    masterRight = Frame(top)

    masterLeft.pack(side=LEFT)
    masterCenter.pack(side=BOTTOM)
    masterRight.pack(side=RIGHT)

    # fill left side
    modeButton = Button(masterLeft, text="address/value", width=5)
    modeButton.place(in_=masterLeft, anchor="c", relx=0.5, rely=0.5)

    # fill middle
    # middle Frame will have four sub-Frames -- four rows of eight buttons.
    fourRows = [Frame(masterCenter) for i in range(4)]
    allButtons = [] # empty for now

    # pack the rows
    for row in fourRows:
        row.pack(side=BOTTOM)

    # fill them with allButtons
    for i in range(4):
        for j in range(8):
            allButtons.append(Button(fourRows[i], text="0", width=5))

    top.mainloop()

if __name__ == "__main__":
    main()