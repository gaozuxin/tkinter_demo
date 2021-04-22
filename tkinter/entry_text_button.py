# !/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk  # 导入 tkinter 库

window = tk.Tk()  # 创建窗口对象的背景色
window.title("my window")
window.geometry("800x800")
e = tk.Entry(window,show=None)
e.pack()
def insert_point():
    var =e.get()
    t.insert('insert',var)
def insert_end():
    var =e.get()
    t.insert(2.2,var)
b1 = tk.Button(window, text="insert point", width=15, height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text="insert point", width=15, height=2, command=insert_end)
b2.pack()
t = tk.Text(window, height=5)
t.pack()
window.mainloop()
