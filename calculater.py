# s = input('input s:')
# r = eval(s)#可接收表达式参数
# print(r)


import tkinter as tk1
import winsound


# 功能
def append_num(i):
    lists.append(i)
    result.set(''.join(lists))  # join 拼接字符串 ''表示字符串
    # winsound.PlaySound("sounds/beep.wav", 1)
    # winsound.PlaySound(winsound.Beep(1600, 500), 1)


def operator(i):
    if len(lists) > 0:
        if lists[-1] in ['+', '-', '*', '/']:
            lists[-1] = i
        else:
            lists.append(i)
    result.set(''.join(lists))


def clear():
    lists.clear()
    result.set(0)

def backspace():
    if lists:
        del lists[-1]
        result.set(''.join(lists))

    else:
        # lists.append('0')
        result.set(0)


# 注意StringVar类型与数字类型的区别
def equal():
    a = ''.join(lists)
    endnum = eval(a)
    print(type(endnum))
    result.set(endnum)
    print(type(result))
    lists.clear()
    lists.append(str(endnum))
    print(lists)


# 界面
# 实例化窗口对象
root = tk1.Tk()
root.title('计算器')
# 设置初始尺寸位置
root.geometry("295x275+1600+500")
# 透明度
# root.attributes("-alpha", 0.7)
# 背景可用图片
root['background'] = "#de3163"
# tkinter特有变量 字符串变量
lists = []
result = tk1.StringVar()
result.set(0)
# 标签
display = tk1.Label(root, textvariable=result, width=32, height=2, justify='left', background='#fff0f5', anchor='e')
# 布局
display.grid(row=0, column=0, columnspan=4)
# 按钮
button_clear = tk1.Button(root, text="CLR", width=5, background='#ffc0cb', bd=0, command=lambda: clear())
button_back = tk1.Button(root, text="DEL", width=5, background='#ffc0cb', bd=0, command=lambda: backspace())
button_division = tk1.Button(root, text="/", width=5, background='#ffc0cb', bd=0, command=lambda: operator('/'))
button_multiplication = tk1.Button(root, text="*", width=5, background='#ffc0cb', bd=0, command=lambda: operator('*'))

button_clear.grid(row=1, column=0, ipadx=4, pady=4)
button_back.grid(row=1, column=1, ipadx=4, pady=4)
button_division.grid(row=1, column=2, ipadx=4, pady=4)
button_multiplication.grid(row=1, column=3, ipadx=4, pady=4)

button_7 = tk1.Button(root, text="7", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('7'))
button_8 = tk1.Button(root, text="8", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('8'))
button_9 = tk1.Button(root, text="9", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('9'))
button_minus = tk1.Button(root, text="-", width=5, background='#ffc0cb', bd=0, command=lambda: operator('-'))

button_7.grid(row=2, column=0, ipadx=4, pady=4)
button_8.grid(row=2, column=1, ipadx=4, pady=4)
button_9.grid(row=2, column=2, ipadx=4, pady=4)
button_minus.grid(row=2, column=3, ipadx=4, pady=4)

button_4 = tk1.Button(root, text="4", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('4'))
button_5 = tk1.Button(root, text="5", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('5'))
button_6 = tk1.Button(root, text="6", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('6'))
button_plus = tk1.Button(root, text="+", width=5, background='#ffc0cb', bd=0, command=lambda: operator('+'))

button_4.grid(row=3, column=0, ipadx=4, pady=4)
button_5.grid(row=3, column=1, ipadx=4, pady=4)
button_6.grid(row=3, column=2, ipadx=4, pady=4)
button_plus.grid(row=3, column=3, ipadx=4, pady=4)

button_1 = tk1.Button(root, text="1", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('1'))
button_2 = tk1.Button(root, text="2", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('2'))
button_3 = tk1.Button(root, text="3", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('3'))
button_equal = tk1.Button(root, text="=", width=5,height=3, background='#ffc0cb', bd=0, command=lambda: equal())

button_1.grid(row=4, column=0, ipadx=4, pady=4)
button_2.grid(row=4, column=1, ipadx=4, pady=4)
button_3.grid(row=4, column=2, ipadx=4, pady=4)
button_equal.grid(row=4, column=3, rowspan=2, ipadx=4, pady=4)

button_null = tk1.Button(root, text=" ", width=5, background='#ffc0cb', bd=0,)
button_0 = tk1.Button(root, text="0", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('0'))
button_point = tk1.Button(root, text=".", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('.'))

button_null.grid(row=5, column=0, ipadx=4, pady=4)
button_0.grid(row=5, column=1, ipadx=4, pady=4)
button_point.grid(row=5, column=2, ipadx=4, pady=4)

# 消息循环
root.mainloop()  # 一直显示
