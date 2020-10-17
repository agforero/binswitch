#!/usr/bin/env python3

import tkinter as tk
import tkinter.font as tkFont
import time
import sys

def binToInt(sequence):
    s = [int(sequence[i]) for i in range(len(sequence))][::-1]
    ret = 0
    for i, n in enumerate(s):
        ret += ((2**i) * n)
    return str(ret)

class OutputApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("BSC text editor")

        # text field
        self.uni = tkFont.Font(family="Courier", size=8)
        self.field = tk.Text(self, height=40, font=self.uni, width=64)
        self.field.pack(side=tk.TOP)

        # current address and char
        self.botDisplay = tk.Frame(self)
        self.botDisplay.pack(side=tk.BOTTOM)

        # declaring elements
        self.addressLabel = tk.Label(self.botDisplay, text="current address: ")
        self.addressDisp = tk.Text(self.botDisplay, height=1, width=10)

        self.charLabel = tk.Label(self.botDisplay, text="current char: ")
        self.charDisp = tk.Text(self.botDisplay, height=1, width=10)

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

        self.addressDisp.delete("1.0", tk.END)
        self.charDisp.delete("1.0", tk.END)

        self.addressDisp.insert(tk.END, binToInt(self.data[0]))
        self.charDisp.insert(tk.END, binToInt(self.data[1]))

        self.after(10, self.updateText)

        f.close()

if __name__ == "__main__":
    app = OutputApp()
    app.mainloop()