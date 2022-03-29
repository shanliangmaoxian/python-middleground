import tkinter as tk
import tkinter.simpledialog as simpledialog
from tkinter import W, E


class Dialog(simpledialog.Dialog):

    def __init__(self, parent):
        l_date = tk.Label(parent, text='时间：')
        l_date.grid(row=0, sticky=E)
        e_date = tk.Entry(parent)
        e_date.grid(row=0, column=1, sticky=W)

        l_title = tk.Label(parent, text='分类：')
        l_title.grid(row=1, sticky=E)
        e_title = tk.Entry(parent)
        e_title.grid(row=1, column=1, sticky=W)

        l_content = tk.Label(parent, text='内容：')
        l_content.grid(row=2, sticky=E)
        e_content = tk.Text(parent, width=25, height=10, undo=True, autoseparators=False)
        e_content.grid(row=2, column=1, sticky=W)

        tk.Button(parent, text='确定').grid(row=3, column=0, sticky="nsew", columnspan=2)

        parent.columnconfigure(0, weight=1)
        parent.columnconfigure(1, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.rowconfigure(1, weight=1)
        parent.rowconfigure(2, weight=1)

        self.body(parent)

    # 设置窗口参数
    def body(self, parent):
        parent.title("综合")
        # 设置窗口大小
        width = 260
        height = 280
        screenwidth = parent.winfo_screenwidth()
        screenheight = parent.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        parent.geometry(alignstr)
        parent.resizable(height=True, width=True)