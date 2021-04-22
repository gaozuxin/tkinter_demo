# !/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import tkinter as tk  # 导入 tkinter 库
from tkinter import ttk, filedialog, messagebox
from tkinter import *

from myRequest import request_get, request_post


def test():
    messagebox.showinfo(title="提示", message="功能暂未开放")


def my_menu():
    menu_bar = tk.Menu(root)   # 创建一个顶层菜单
    submenu1 = tk.Menu(menu_bar, tearoff=0)  # 创建menu菜单的子菜单,tearoff=False 表示这个菜单可以被拖拽出来
    menu_bar.add_cascade(label='文件', menu=submenu1)  # 添加menu菜单的内容
    submenu1.add_command(label="新建", command=test)  # 添加filemenu子菜单的内容
    submenu1.add_command(label="打开", command=test)
    submenu1.add_command(label="保存", command=test)
    submenu1.add_separator()  # 一个下拉菜单的分割线
    submenu1.add_command(label="导入", command=test)
    submenu1.add_command(label="导出", command=test)
    submenu1.add_separator()  # 一个下拉菜单的分割线
    submenu1.add_cascade(label="退出", command=root.quit())

    submenu2 = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='功能', menu=submenu2)
    submenu2.add_command(label="接口测试", command=test)
    submenu2.add_command(label="性能测试", command=test)
    submenu2.add_command(label="自动化测试", command=test)

    submenu3 = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="帮助", menu=submenu3)
    submenu3.add_command(label="查看帮助", command=test)
    # submenu3.add_separator()
    submenu3.add_command(label="关于", command="")
    # submenu3_1 = tk.Menu(submenu3)
    # submenu3.add_cascade(label="Test", menu=submenu3_1, underline=0)
    # submenu3_1.add_command(label="Submenu1", command=test)
    # submenu3_1.add_command(label="Submenu2", command=test)
    root.config(menu=menu_bar)  # 将root根窗口的顶级菜单设置为menu


def my_frame():
    def send_top1():
        treq_method = comb_top.get()
        treq_url = et_top.get()
        treq_hearders = hearders_text.get('0.0', END).strip()
        treq_input = input_text.get('0.0', END).strip()

        print("请求方式：" + treq_method + "\n请求url:" + treq_url + "\n入参" + treq_input)
        if treq_method == "GET":
            if treq_url == "":
                messagebox.showinfo(title="提示", message="请输入URL")
            elif treq_url.startswith("http://") or treq_url.startswith("https://"):
                headers = {}
                if treq_hearders == "":
                    pass
                elif treq_hearders.startswith("{") and treq_hearders.endswith("}"):
                    headers = treq_hearders
                else:
                    pass  # headers 特殊处理
                r = request_get(treq_url, headers)
                print(r.status_code)
                print(r.text)
            else:
                messagebox.showinfo(title="提示", message="请输入正确的URL")
        elif treq_method == "POST":
            if treq_url == "":
                messagebox.showinfo(title="提示", message="请输入URL")
            elif treq_url.startswith("http://") or treq_url.startswith("https://"):
                headers = {}

                # 判断请求hearders
                if treq_hearders == "":
                    headers ={"Content-Type":"application/json"}  # 默认application

                    formdata = ""
                    print("类型{}".format(type(treq_input)))
                    if treq_input.startswith("{") and treq_input.endswith("}"):
                        formdata = treq_input
                    elif treq_input == "":
                        messagebox.showinfo(title="提示", message="请输入接口入参")
                    else:
                        messagebox.showinfo(title="提示", message="请输入正确的接口入参")
                        print(treq_input)
                    r = request_post(treq_url, headers, formdata)
                    print(r.status_code)
                    print(r.text)

                elif treq_hearders.startswith("{") and treq_hearders.endswith("}"):
                    headers = treq_hearders

                    formdata = ""
                    print("类型{}".format(type(treq_input)))
                    if treq_input.startswith("{") and treq_input.endswith("}"):
                        formdata = treq_input
                    elif treq_input == "":
                        messagebox.showinfo(title="提示", message="请输入接口入参")
                    else:
                        messagebox.showinfo(title="提示", message="请输入正确的接口入参")
                        print(treq_input)
                    r = request_post(treq_url, headers, formdata)
                    print(r.status_code)
                    print(r.text)

                else:
                    print("请输入正确的hearders")
                    pass  # headers 特殊处理

                # 判断输入文本
        else:
            messagebox.showinfo(title="提示", message="请选择请求方式")

    def open_file():
        file_name = filedialog.askopenfilename(
            filetypes=[("PNG", ".png"), ("GPF", ".gpf"), ("JPG", ".jpg"), ("python", ".py"), ("EXE", ".exe")])
        et_bottom.delete(0, END)
        et_bottom.insert('insert', file_name)

    frm_top = tk.Frame(root)
    frm_left1 = tk.Frame(root)
    frm_left2 = tk.Frame(root)
    frm_right = tk.Frame(root)
    frm_bottom = tk.Frame(root)
    frm_bg = "#F0F0F0"
    btn_bg = "#4876FF"

    frm_top.config(bg=frm_bg, height=40, width=1090)
    frm_top.place(x=5, y=5)
    # 设置请求方式下拉框
    req_method = tk.StringVar()
    comb_top = ttk.Combobox(frm_top, width=10, height=9, textvariable=req_method, state='readonly')
    comb_top['values'] = ("GET", "POST")  # 设置下拉列表的值
    comb_top.place(x=10, y=10)  # 设置其在界面中出现的位置 column代表列 row 代表行
    # comb.grid(column=1, row=1)
    comb_top.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
    # 设置请求url
    req_url = tk.StringVar()
    et_top = tk.Entry(frm_top, width=90, textvariable=req_url, relief="solid")
    et_top.place(x=120, y=11)
    et_top.insert(0, "请求url...")

    btn_top1 = tk.Button(frm_top, text="Send", bg=btn_bg, font='Verdana 9 bold', width=8, command=send_top1)
    btn_top1.place(x=850, y=10)

    btn_top2 = tk.Button(frm_top, text="Save", bg="#C4C4C4", font='Verdana 9 bold',  width=8, command=test)
    btn_top2.place(x=950, y=10)

    frm_left1.config(bg=frm_bg, height=260, width=435)
    tk.Label(frm_left1, text='hearders').place(anchor=NW)
    frm_left1.place(x=5, y=50)
    # 设置入参文本框
    hearders_text = tk.Text(frm_left1, width='58', height='17')
    hearders_text.place(x=10, y=25)

    frm_left2.config(bg=frm_bg, height=380, width=435)
    tk.Label(frm_left2, text='input').place(anchor=NW)
    frm_left2.place(x=5, y=315)
    # 设置入参文本框
    input_text = tk.Text(frm_left2, width='58', height='26')
    input_text.place(x=10, y=25)

    frm_right.config(bg=frm_bg, height=645, width=650)
    tk.Label(frm_right, text='output').place(in_=frm_right, anchor=NW)
    tk.Label(frm_right, text='响应结果', fg='red', font='Verdana 10 bold').place(x=100, y=50, height=80, width=400)
    frm_right.place(x=445, y=50)
    # 设置出参文本框
    output_text = tk.Text(frm_right, width='89', height='47')
    output_text.place(x=10, y=25)

    frm_bottom.config(bg=frm_bg, height=40, width=1090)
    frm_bottom.place(x=5, y=700)
    # 选择文件按钮
    btn_bottom = tk.Button(frm_bottom, text="Openfile", command=open_file, font='Verdana 9 ')
    btn_bottom.place(x=15, y=10)

    filename = StringVar()
    et_bottom = tk.Entry(frm_bottom, width=90, textvariable=filename, relief="solid")
    et_bottom.place(x=100, y=11)
    et_bottom.insert(0, "请选择文件...")

    btn_bottom = tk.Button(frm_bottom, text="execute", bg=btn_bg, font='Verdana 9 bold', width=8, command=test)
    btn_bottom.place(x=800, y=10)


if __name__ == '__main__':
    root = tk.Tk()  # 创建窗口对象的背景色
    root.iconbitmap(os.path.dirname(__file__) + "/image/{}".format("shanghuiyun.ico"))  # 添加窗口图标
    root.title("TestTools")
    root.geometry("1100x760+150+20")  # 设置窗口大小  并初始化桌面位置
    # window.geometry("{}x{}".format(window.winfo_screenwidth(), window.winfo_screenheight()))  #  界面最大化
    # window.attributes("-topmost",True)
    root.resizable(width=0, height=0)  # 宽不可变 高可变  默认True
    root.configure(background="#ffffff")
    # my_menu()
    my_frame()
    root.mainloop()
