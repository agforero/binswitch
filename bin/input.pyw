#!/usr/bin/env python3

from tkinter import *

# store it in a class so we have access to THIS data in particular
class Data:
    def __init__(self):
        self.addressMode = True # if we're in address mode; False if we're in value node
        self.currentAAV = [["0" for i in range(32)] for j in range(2)] # "current Address and Value"

def swapData(BText, container, idx):
    if container.addressMode: # we're in address mode
        container.currentAAV[0][idx] = 1 if (container.currentAAV[0][idx] == 0) else 0
        BText.set(container.currentAAV[0][idx])

    else: # we're in value mode
        container.currentAAV[1][idx] = 1 if (container.currentAAV[1][idx] == 0) else 0
        BText.set(container.currentAAV[1][idx])

def swapModes(BText, container, allButtons):
    if container.addressMode == True:
        BText.set("value")
        container.addressMode = False
        for i, b in enumerate(allButtons):
            b.txt.set(container.currentAAV[1][i]) # update buttons to be all value components
    else:
        BText.set("address")
        container.addressMode = True
        for i, b in enumerate(allButtons):
            b.txt.set(container.currentAAV[0][i]) # update buttons to be all address components

def submit(container):
    f = open("../data/data.txt", "a")
    
    stringToWrite = ""
    for i in range(2):
        for j in range(32):
            stringToWrite += str(container.currentAAV[i][j])
        stringToWrite += "\t"

    f.write(stringToWrite + "\n")
    f.close()

class BinButton:
    def __init__(self, master, idx, container):
        self.txt = StringVar()
        self.txt.set("0")
        self.idx = idx
        self.B = Button(master, textvariable=self.txt, width=3, command=(lambda: self.swapData(container)))
    
    def swapData(self, container):
        if container.addressMode: # we're in address mode
            container.currentAAV[0][self.idx] = 1 if (container.currentAAV[0][self.idx] == 0) else 0
            self.txt.set(container.currentAAV[0][self.idx])

        else: # we're in value mode
            container.currentAAV[1][self.idx] = 1 if (container.currentAAV[1][self.idx] == 0) else 0
            self.txt.set(container.currentAAV[1][self.idx])

def binToStrInt(sequence):
    s = [int(sequence[i]) for i in range(len(sequence))][::-1]
    ret = 0
    for i, n in enumerate(s):
        ret += ((2**i) * n)
    return str(ret)

def saveData():
    print("saving!")
    f = open("../data/data.txt", "r")

    allText = {}
    for line in f.readlines():
        data = line.split()
        allText[int(binToStrInt(data[0]))] = chr(int(binToStrInt(data[1])))

    writeOut = ""
    sortedKeys = list(allText.keys())
    sortedKeys.sort()
    for k in sortedKeys:
        writeOut += allText[k]

    o = open("output.txt", "w")
    o.write(writeOut)

    f.close()
    o.close()
    

def main():
    # initializing tkinter elements
    top = Tk()
    top.title("BSC input tool")

    f = open("../data/data.txt", "w")

    startString = ""
    for i in range(2):
        for j in range(32):
            startString += "0"
        startString += "\t"
    f.write(startString + "\n")    

    f.close()

    container = Data()

    # left side: one checkbox, toggling address/value modes
    # middle: 4 rows of 8 checkboxes = 32 checkboxes, for entry
    # right: confirmation button, sorta like an Enter key
    masterLeft = Frame(top)
    masterCenter = Frame(top)
    masterRight = Frame(top)

    masterLeft.pack(side=LEFT)
    masterCenter.pack(side=LEFT)
    masterRight.pack(side=LEFT)

    # fill middle
    # middle Frame will have four sub-Frames -- four rows of eight buttons.
    fourRows = [Frame(masterCenter) for i in range(4)]

    for row in fourRows:
        row.pack(side=TOP)

    allButtons = []
    for i in range(4):
        for j in range(8):
            idx = (i * 8) + j
            allButtons.append(BinButton(fourRows[i], idx, container))
            allButtons[idx].B.pack(side=LEFT)

    # fill left side
    modeText = StringVar()
    modeText.set("address")
    modeButton = Button(masterLeft, textvariable=modeText, width=9, command=(lambda: swapModes(modeText, container, allButtons)))
    modeButton.pack(side=BOTTOM)
            
    # fill right side
    enterText = StringVar()
    enterText.set("enter")
    enterButton = Button(masterRight, textvariable=enterText, width=9, command=(lambda: submit(container)))
    enterButton.pack(side=TOP)

    saveText = StringVar()
    saveText.set("save")
    saveButton = Button(masterRight, textvariable=saveText, width=9, command=(lambda: saveData()))
    saveButton.pack(side=TOP)

    top.mainloop()

if __name__ == "__main__":
    main()