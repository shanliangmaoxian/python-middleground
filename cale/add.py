import tkinter as tk
import tkinter.simpledialog as simpledialog

class Dialog(simpledialog.Dialog):
    def __init__(self, parent):
        tk.Label(parent, text="Hello").grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(parent, text="ONE").grid(row=1, column=0, sticky="nsew")
        tk.Button(parent, text="TWO").grid(row=1, column=1, sticky="nsew")

        parent.columnconfigure(0, weight=1)
        parent.columnconfigure(1, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.rowconfigure(1, weight=1)

        # self.resizable(height=True, width=True)