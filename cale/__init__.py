import tkinter as tk
import tkinter.simpledialog as simpledialog


class Dialog(simpledialog.Dialog):

    def __init__(self, parent):
        tk.Label(parent, text='aaa').grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(parent, text='bbb').grid(row=1, column=0, sticky="nsew")
        tk.Button(parent, text='ccc').grid(row=1, column=1, sticky="nsew")

        parent.columnconfigure(0, weight=1)
        parent.columnconfigure(1, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.rowconfigure(1, weight=1)

        self.body(parent)

    # 设置窗口参数
    def body(self, parent):
        parent.title("综合")
        # 设置窗口大小
        width = 500
        height = 250
        screenwidth = parent.winfo_screenwidth()
        screenheight = parent.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        parent.geometry(alignstr)
        parent.resizable(height=True, width=True)