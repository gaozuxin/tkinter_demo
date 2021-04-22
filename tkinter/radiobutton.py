# !/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk  # 导入 tkinter 库

window = tk.Tk()  # 创建窗口对象的背景色
window.title("my window")
window.geometry("800x200+200+100")  # 设置窗口大小  并初始化桌面位置
window.resizable(width = True,height = True)  # 宽不可变 高可变  默认True
var=tk.StringVar()
l = tk.Label(window,bg="yellow",width=20,text="empty")
l.pack()


def print_selection():
    l.config(text="you hava selected "+var.get())


r1=tk.Radiobutton(window,text="Option A",variable=var,value="A",command =print_selection)
r1.pack()
r2=tk.Radiobutton(window,text="Option B",variable=var,value="B",command =print_selection)
r2.pack()
r3=tk.Radiobutton(window,text="Option C",variable=var,value="C",command =print_selection)
r3.pack()

window.mainloop()
