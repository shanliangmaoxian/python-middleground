import datetime
import tkinter as tk
from tkinter import LEFT, N, E, W, S, RIGHT
from datetime import *
from dateutil.relativedelta import relativedelta
import calendar
import sqlite3
import cale as dialog

win = tk.Tk()
win.title("综合")
# 设置窗口大小
width = 1500
height = 750
screenwidth = win.winfo_screenwidth()
screenheight = win.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
win.geometry(alignstr)

weekStr = ['日', '一', '二', '三', '四', '五', '六']

# 新建数据库
conn = sqlite3.connect('ppt')
c = conn.cursor()

localTime = datetime.now()
todayMonty = localTime.strftime("%m")
nowDateStr = tk.StringVar()
yearStr = tk.StringVar()
monthStr = tk.StringVar()
dayStr = tk.StringVar()

# 超过10个字增加换行
def wrap(text):
    lenIdx = 17
    if text == None:
        return ''
    elif len(text) > lenIdx:
        return text[0:lenIdx] + '\n' + wrap(text[lenIdx:])
    return text

def nextMonth():
    initCalendar(
        datetime(int(yearStr.get()), int(monthStr.get()), int(dayStr.get()), 0, 0, 0) + relativedelta(months=+1))


def beforeMonth():
    initCalendar(
        datetime(int(yearStr.get()), int(monthStr.get()), int(dayStr.get()), 0, 0, 0) + relativedelta(months=-1))

def today():
    initCalendar(localTime)

# 弹出新增窗口
def add():
    dialog.Dialog(tk.Tk())

# 在窗口内创建按钮，以表格的形式依次排列

frame = tk.Frame(win)
tk.Button(frame, text=">", command=nextMonth).pack(side=RIGHT, padx="0", pady="0")
tk.Button(frame, text="今天", command=today).pack(side=RIGHT, padx="0", pady="0")
tk.Button(frame, text="<", command=beforeMonth).pack(side=RIGHT, padx="0", pady="0")
tk.Button(frame, text="新增", command=add).pack(side=RIGHT, padx="2", pady="0")
frame.grid(row=0, column=5, columnspan=2, sticky=E)

calendar.setfirstweekday(firstweekday=6)

for i in range(7):
    tk.Label(win, text="周" + weekStr[i], width=int(width / 7)).grid(row=1, column=i)


frameArr = []
def initCalendar(localTime):
    nowDateStr.set(localTime.strftime("%Y年%m月"))
    yearStr.set(localTime.strftime("%Y"))
    monthStr.set(localTime.strftime("%m"))
    dayStr.set(localTime.strftime("%d"))

    tk.Label(win, text=nowDateStr.get(), justify=LEFT, font=("华文行楷", 22)).grid(row=0, column=0, columnspan=1)

    # 得到所有的记录
    rec = c.execute(
        '''select * from calendar where date like ('%-''' + monthStr.get() + '''-%')''')
    resData = rec.fetchall()
    # 销毁
    for i in range(len(frameArr)):
        frameArr[i].destroy()
    frameArr.clear()

    dateArr = calendar.monthcalendar(int(yearStr.get()), int(monthStr.get()))
    # 新建对象
    for i in range(len(dateArr)):
        for j in range(7):
            frame = tk.Frame(win, height=height / 9, highlightbackground="gray", highlightthickness=1)
            idx = 0
            if dateArr[i][j] > 0:
                label1 = tk.Label(frame, text=dateArr[i][j], justify=LEFT)
                label1.grid(row=idx, column=0)

                arr = [elem for elem in resData if int(elem[1][8:]) == dateArr[i][j]]
                for item in arr:
                    idx = idx + 1
                    tk.Label(frame, text=wrap('[' + item[1][0:4] + ']' + item[4]), font=("华文行楷", 12), justify=LEFT).grid(row=idx, column=1, sticky='w')

                # 如果今天修改 背景色
                if dateArr[i][j] == int(dayStr.get()) and todayMonty == monthStr.get():
                    label1.configure(bg="red")
            frame.grid(row=i + 2, column=j, sticky=(N, E, W, S))
            frameArr.append(frame)
    # 进入消息循环
    for i in range(2, len(dateArr) + 2):
        win.rowconfigure(i, weight=1)

    for j in range(7):
        win.columnconfigure(j, weight=1)


initCalendar(datetime.now())

win.mainloop()
