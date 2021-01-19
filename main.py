'''
    CSV生成器
    开始编写日期：2021年1月19日
    作者：张懿嘉
'''

import csv
import tkinter as tk


if __name__ == "__main__":
    # 初始化
    window = tk.Tk()
    window.title("CSV Maker")
    window.geometry("600x500")
    var = 0
    def add():
        global var
        var = var+1
        print(var)
    def reset():
        global var
        var = 0
        print(var)
    button1 = tk.Button(window, text="属性1", width=10,
                        height=1, command=add)
    button1.pack()
    button2 = tk.Button(window, text="清零", width=10,
                        height=1, command=reset)
                        tk.messagebox.showinfo("提示",message="清零成功!")
    button2.pack()
    # 主窗口显示
    window.mainloop()
    # print("ssss")

  

    pass
