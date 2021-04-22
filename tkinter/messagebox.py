# !/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk  # 导入 tkinter 库
import tkinter.messagebox

window = tk.Tk()  # 创建窗口对象的背景色
window.title("my window")
window.geometry("800x200+200+100")  # 设置窗口大小  并初始化桌面位置
window.resizable(width=True, height=True)  # 宽不可变 高可变  默认True
def hit_me():
    tk.messagebox.showinfo(title="Hi",message="哈哈哈哈哈")
    tk.messagebox.showwarning(title="Hi",message="nonononono")
    tk.messagebox.showerror(title="Hi",message="No!!never")
    tk.messagebox.askquestion(title="Hi",message="No!!never" ) # reyurn  'yes',"no"
    print(tk.messagebox.askquestion(title="Hi",message="No!!never" )) # reyurn  'yes',"no"
    print(tk.messagebox.askyesno(title="Hi",message="No!!never" )) # reyurn  'Ture',"Flase"
    print(tk.messagebox.askretrycancel(title="Hi",message="No!!never" )) # reyurn  'Ture',"Flase"
    print(tk.messagebox.askokcancel(title="Hi",message="No!!never" )) # reyurn  'Ture',"Flase"


tk.Button(window,text="hit me",command=hit_me).pack()
window.mainloop()