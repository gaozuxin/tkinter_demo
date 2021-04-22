# !/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk  # 导入 tkinter 库
import tkinter.messagebox

window = tk.Tk()  # 创建窗口对象的背景色
window.title("my window")
window.geometry("800x200+200+100")  # 设置窗口大小  并初始化桌面位置
window.resizable(width=True, height=True)  # 宽不可变 高可变  默认True
# tk.Label(window,text=1).pack(side="top")
# tk.Label(window,text=2).pack(side="bottom")
# tk.Label(window,text=3).pack(side="left")
# tk.Label(window,text=4).pack(side="right")


# for i in range(4):
#     for j in range(3):
#         tk.Label(window,text=1).grid(row=i,column=j,padx=10,pady=10)
#         tk.Label(window,text=1).grid(row=i,column=j,ipadx=10,ipady=10)

tk.Label(window,text=1).place(x=10,y=100,anchor='nw')



window.mainloop()