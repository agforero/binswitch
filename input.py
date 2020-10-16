#!/usr/bin/env python3

from tkinter import *

# store it in a class so we have access to THIS data in particular
class Data:
    def __init__(self):
        self.currentAAV = [["0" for i in range(32)] for j in range(2)] # "current Address and Value"

def swapData(B, mode, container, idx):
    if mode: # we're in address mode
        container.currentAAV[0][idx]

    else: # we're in value mode
        pass

def main():
    # initializing tkinter elements
    top = Tk()
    top.title("BSC input tool")

    container = Data()
    addressMode = True # if we're in address mode; False if we're in value node

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
    modeButton = Button(masterLeft, text="address/\nvalue", width=5)
    modeButton.pack(side=BOTTOM)

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
            buttonText = StringVar()
            allButtons.append(Button(fourRows[i], textvariable=buttonText, width=5))
            allButtons[-1].pack(side=LEFT)
            buttonText.set("0")

    top.mainloop()

if __name__ == "__main__":
    main()