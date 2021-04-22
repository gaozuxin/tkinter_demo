# !/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk  # 导入 tkinter 库

window = tk.Tk()  # 创建窗口对象的背景色
window.title("my window")
window.geometry("800x200+200+100")  # 设置窗口大小  并初始化桌面位置
window.resizable(width = True,height = True)  # 宽不可变 高可变  默认True

l = tk.Label(window,bg="yellow",width=20,text="empty")
l.pack()


def print_selection():
    if(var1.get()==1)&(var2.get()==0):
        l.config(text="I love only Python")
    elif(var1.get()==0)&(var2.get()==1):
        l.config(text="I love only C++")
    elif (var1.get() == 1) & (var2.get() == 1):
        l.config(text="I love both")
    else:
        l.config(text="I do not love either")

var1=tk.IntVar()
var2=tk.IntVar()
c1 =tk.Checkbutton(window,text="Python",variable=var1,onvalue=1,offvalue=0,command =print_selection)
c2 =tk.Checkbutton(window,text="c++",variable=var2,onvalue=1,offvalue=0,command =print_selection)
c1.pack()
c2.pack()
window.mainloop()
