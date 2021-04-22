# !/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk  # 导入 tkinter 库

window = tk.Tk()  # 创建窗口对象的背景色
window.title("my window")
window.geometry("800x200+200+100")  # 设置窗口大小  并初始化桌面位置
window.resizable(width=True, height=True)  # 宽不可变 高可变  默认True
tk.Label(window,text="on the window").pack()


frm =tk.Frame(window)
frm.pack()
frm_l=tk.Frame(frm,)
frm_r = tk.Frame(frm)
frm_l.pack(side='left')
frm_r.pack(side='right')
tk.Label(frm_l,text="on the frm_l1").pack()
tk.Label(frm_l,text="on the frm_l2").pack()
tk.Label(frm_r,text="on the frm_r1").pack()

window.mainloop()
