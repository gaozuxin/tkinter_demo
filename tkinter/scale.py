# !/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk  # 导入 tkinter 库

window = tk.Tk()  # 创建窗口对象的背景色
window.title("my window")
window.geometry("800x200+200+100")  # 设置窗口大小  并初始化桌面位置
window.resizable(width = True,height = True)  # 宽不可变 高可变  默认True

l = tk.Label(window,bg="yellow",width=20,text="empty")
l.pack()


def print_selection(v):
    l.config(text="you hava selected "+v)



s=tk.Scale(window,label="try me",from_=5,to=11,orient =tk.HORIZONTAL,length=200,
           showvalue=0,tickinterval=2,resolution=0.01,command=print_selection)
s.pack()
window.mainloop()
