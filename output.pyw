#!/usr/bin/env python3

import tkinter as tk
import tkinter.font as tkFont
import time
import sys

def binToStrInt(sequence):
    s = [int(sequence[i]) for i in range(len(sequence))][::-1]
    ret = 0
    for i, n in enumerate(s):
        ret += ((2**i) * n)
    return str(ret)

class FieldText():
    def __init__(self):
        self.text = {}

    def getText(self):
        if len(list(self.text.keys())) == 0: return ""

        ret = ""
        sortedKeys = list(self.text.keys())
        sortedKeys.sort()

        for k in sortedKeys:
            ret += self.text[k]

        print(ret) 
        return ret

    def updateText(self, data):
        self.address = int(binToStrInt(data[0]))
        self.char = chr(int(binToStrInt(data[1]))) if (int(binToStrInt(data[1])) < 127) else "OUT OF RANGE"

        self.text[self.address] = self.char

class OutputApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("BSC text editor")

        # text field
        self.uni = tkFont.Font(family="Courier", size=8)
        self.field = tk.Text(self, height=40, font=self.uni, width=64)
        self.field.pack(side=tk.TOP)
        self.fieldText = FieldText()

        # current address and char
        self.botDisplay = tk.Frame(self)
        self.botDisplay.pack(side=tk.BOTTOM)

        # declaring elements
        self.addressLabel = tk.Label(self.botDisplay, text="current address: ")
        self.addressDisp = tk.Text(self.botDisplay, height=1, width=12)

        self.charLabel = tk.Label(self.botDisplay, text="current char: ")
        self.charDisp = tk.Text(self.botDisplay, height=1, width=12)

        # packing elements in order
        self.addressLabel.pack(side=tk.LEFT)
        self.addressDisp.pack(side=tk.LEFT)

        self.charDisp.pack(side=tk.RIGHT)
        self.charLabel.pack(side=tk.RIGHT)
        
        self.updateText()

    def updateText(self):
        f = open("data.txt", "r")

        try: self.data = f.readlines()[-1].split()
        except: sys.exit(0)

        # update big text field
        self.fieldText.updateText(self.data)
        self.field.delete("1.0", tk.END)
        self.field.insert(tk.END, self.fieldText.getText())

        # update info bars
        self.addressDisp.delete("1.0", tk.END)
        self.charDisp.delete("1.0", tk.END)

        self.addressDisp.insert(tk.END, binToStrInt(self.data[0]))
        self.charDisp.insert(tk.END, binToStrInt(self.data[1]))

        self.after(10, self.updateText)

        f.close()

if __name__ == "__main__":
    app = OutputApp()
    app.mainloop()