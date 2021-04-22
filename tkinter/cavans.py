# !/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk  # 导入 tkinter 库

window = tk.Tk()  # 创建窗口对象的背景色
window.title("my window")
window.geometry("800x200+200+100")  # 设置窗口大小  并初始化桌面位置
window.resizable(width = True,height = True)  # 宽不可变 高可变  默认True

canvas = tk.Canvas(window,bg="blue",height=100,width=200)
image_file = tk.PhotoImage(file="ins.gif")
image=canvas.create_image(0,0,anchor='nw',image=image_file)
x0,y0,x1,y1=50,50,80,80
line = canvas.create_line(x0,y0,y1,y1)
oval =canvas.create_oval(x0,y0,x1,y1,fill="red")
arc =canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start=0,extent=180)
rect =canvas.create_rectangle(100,30,120,20+30)


canvas.pack()

def moveit():
    canvas.move(rect,0,2)  # 移动正方形

b =tk.Button(window,text="move",command=moveit).pack()
window.mainloop()
