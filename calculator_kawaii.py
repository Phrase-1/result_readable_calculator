
import tkinter as tk
from tkinter.messagebox import askyesno
import tkinter.messagebox
import winsound
import random
import threading
import time


class ResultReadThread(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        time.sleep(0.7)  # 为使等于号的语音不被打断
        speak_result(self.number)


def init():
    voice_lists = ['スタート', '起動します', '起動するよ', '始まるよ～', '呼びました？', 'はいは～い', '呼んだかな？']
    i = voice_lists[random.randint(0, 6)]
    url = "sounds\\" + i + ".wav"
    winsound.PlaySound(url, 1)


def speak_num(i):
    if i == 'DEL':
        i = str(random.randint(1, 3))
        url = "sounds\\疑問" + i + ".wav"
        winsound.PlaySound(url, 1)
    elif i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        url = "sounds\\" + i + ".wav"
        winsound.PlaySound(url, 1)
    else:
        i = switch_symbol(i)
        url = "sounds\\" + i + ".wav"
        winsound.PlaySound(url, 1)


# 正数 负数 0
# 整数 小数
# 绝对值 > 1 绝对值 < 1
def speak_result(i):
    tail_list = ['でした', 'です', 'だよ']
    tail_voice_filename = tail_list[random.randint(0, 2)]
    tail_voice_url = "sounds\\" + tail_voice_filename + ".wav"
    speak_list = []
    if i == 0:
        speak_list.append('sounds/0.wav')
        speak_list.append(tail_voice_url)
        for item in speak_list:  # 开新线程
            winsound.PlaySound(item, 65536)
        return
    int_part = int(i)
    float_part = i - int_part
    number_list = []
    int_part_temp = abs(int_part)
    while int_part_temp >= 1:
        number_list.append(int_part_temp % 10)
        int_part_temp = int(int_part_temp / 10)
    length = len(number_list)  # 通过长度得知数位
    if length <= 8:
        if i < 0:
            speak_list.append('sounds/ひく.wav')
        while length in range(5, 9):  # 处理万级部分
            list_temp = list(reversed(number_list[4:8]))  # 将万级部分反转并放入temp中
            length_temp = length
            for x in range(0, len(list_temp)):
                if list_temp[x] == 0:  # 对于日语中数字读法的考虑，若使用中文读法，删去此句
                    length_temp -= 1
                    continue
                n = (length_temp % 5)  # 对4取余加1 求10的次幂
                url = "sounds/" + str(list_temp[x] * pow(10, n)) + ".wav"
                speak_list.append(url)
                length_temp -= 1
            # print(speak_list)
            speak_list.append('sounds/万.wav')
            break
        # while length in range(1, 5):  # 处理个级部分
        # list_temp.clear()
        list_temp = list(reversed(number_list[0:4]))  # 将个级部分反转并放入temp中
        length_temp = len(list_temp)
        for x in range(0, len(list_temp)):
            if list_temp[x] == 0:  # 对于日语中数字读法的考虑，若使用中文读法，删去此句
                length_temp -= 1
                continue
            n = (length_temp % 5) - 1  # 对4取余加1 求10的次幂
            url = "sounds/" + str(list_temp[x] * pow(10, n)) + ".wav"
            speak_list.append(url)
            length_temp -= 1
    else:
        winsound.PlaySound('sounds/結果を発表します.wav', 65536)
    float_part_temp = abs(float_part)
    if float_part_temp > 0:  # 若存在小数部分
        if abs(i) < 1:  # 若待读数绝对值小于1
            speak_list.append('sounds/0.wav')
        speak_list.append('sounds/..wav')
        float_part_temp *= 10
        float_number_list = []
        for j in range(0, 6):  # 读小数点后六位
            float_number_list.append(int(float_part_temp))
            float_part_temp -= int(float_part_temp)
            float_part_temp *= 10
        for item in float_number_list:
            url = "sounds/" + str(item) + ".wav"
            speak_list.append(url)
    speak_list.append(tail_voice_url)
    for item in speak_list:  # 开新线程
        winsound.PlaySound(item, 65536)


def switch_symbol(argument):
    switcher = {
        '+': "たす",
        '-': "ひく",
        '*': "かける",
        '/': "割る",
        '=': "イコール",
        'CLR': "ゲームセット",
        ' ': "いないいない"
    }
    return switcher.get(argument)


# 功能
def append_num(i):
    lists.append(i)
    result.set(''.join(lists))  # join 拼接字符串 ''表示字符串
    speak_num(i)


def operator(i):
    if len(lists) > 0:
        if lists[-1] in ['+', '-', '*', '/']:
            lists[-1] = i
        else:
            lists.append(i)
    result.set(''.join(lists))
    speak_num(i)


def clear():
    lists.clear()
    result.set(0)
    speak_num('CLR')


def backspace():
    if lists:
        del lists[-1]
        result.set(''.join(lists))
    else:
        # lists.append('0')
        result.set(0)
    speak_num('DEL')


# 注意StringVar类型与数字类型的区别
def equal():
    speak_num('=')
    a = ''.join(lists)
    endnum = eval(a)
    result.set(endnum)
    lists.clear()
    lists.append(str(endnum))
    speak_thread = ResultReadThread(endnum)
    speak_thread.start()


def close_window():
    voice_lists = ['また遊んでね', 'あれれ、もう終わっちゃうの？', 'お疲れ様でした', 'お疲れ様です', 'それじゃね', 'バイバーイ', 'また明日']
    i = voice_lists[random.randint(0, 6)]
    url = "sounds\\" + i + ".wav"
    winsound.PlaySound(url, 1)
    quit1 = tkinter.messagebox.askokcancel('提示', '真的要退出吗？')
    if quit1:
        root.destroy()
    # ans = askyesno(title='Warning', message='Close the window?')
    # if ans:
    #     root.destroy()
    # else:
    #     return


init()
# 界面
# 实例化窗口对象
root = tk.Tk()
root.title('计算器')
root.iconbitmap('img/icon2.ico')
# 设置初始尺寸位置
root.geometry("294x285+1000+500")
# 透明度
# root.attributes("-alpha", 0.7)
# 背景可用图片
root['background'] = "#fff0f5"
# tkinter特有变量 字符串变量
lists = []
result = tk.StringVar()
result.set(0)
# 标签
display = tk.Label(root, textvariable=result, width=32, height=2, justify='left', background='#fff0f5', anchor='e')
# 布局
display.grid(row=0, column=0, columnspan=4)
# 按钮
button_clear = tk.Button(root, text="CLR", width=5, background='#ffc0cb', bd=0, command=lambda: clear())
button_back = tk.Button(root, text="DEL", width=5, background='#ffc0cb', bd=0, command=lambda: backspace())
button_division = tk.Button(root, text="/", width=5, background='#ffc0cb', bd=0, command=lambda: operator('/'))
button_multiplication = tk.Button(root, text="*", width=5, background='#ffc0cb', bd=0, command=lambda: operator('*'))

button_clear.grid(row=1, column=0, ipadx=4, pady=4)
button_back.grid(row=1, column=1, ipadx=4, pady=4)
button_division.grid(row=1, column=2, ipadx=4, pady=4)
button_multiplication.grid(row=1, column=3, ipadx=4, pady=4)

button_7 = tk.Button(root, text="7", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('7'))
button_8 = tk.Button(root, text="8", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('8'))
button_9 = tk.Button(root, text="9", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('9'))
button_minus = tk.Button(root, text="-", width=5, background='#ffc0cb', bd=0, command=lambda: operator('-'))

button_7.grid(row=2, column=0, ipadx=4, pady=4)
button_8.grid(row=2, column=1, ipadx=4, pady=4)
button_9.grid(row=2, column=2, ipadx=4, pady=4)
button_minus.grid(row=2, column=3, ipadx=4, pady=4)

button_4 = tk.Button(root, text="4", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('4'))
button_5 = tk.Button(root, text="5", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('5'))
button_6 = tk.Button(root, text="6", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('6'))
button_plus = tk.Button(root, text="+", width=5, background='#ffc0cb', bd=0, command=lambda: operator('+'))

button_4.grid(row=3, column=0, ipadx=4, pady=4)
button_5.grid(row=3, column=1, ipadx=4, pady=4)
button_6.grid(row=3, column=2, ipadx=4, pady=4)
button_plus.grid(row=3, column=3, ipadx=4, pady=4)

button_1 = tk.Button(root, text="1", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('1'))
button_2 = tk.Button(root, text="2", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('2'))
button_3 = tk.Button(root, text="3", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('3'))
button_equal = tk.Button(root, text="=", width=5, height=3, background='#ffc0cb', bd=0, command=lambda: equal())

button_1.grid(row=4, column=0, ipadx=4, pady=4)
button_2.grid(row=4, column=1, ipadx=4, pady=4)
button_3.grid(row=4, column=2, ipadx=4, pady=4)
button_equal.grid(row=4, column=3, rowspan=2, ipadx=4, pady=4)

button_null = tk.Button(root, text=" ", width=5, background='#ffc0cb', bd=0, command=lambda: speak_num(' '))
button_0 = tk.Button(root, text="0", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('0'))
button_point = tk.Button(root, text=".", width=5, background='#ffc0cb', bd=0, command=lambda: append_num('.'))

button_null.grid(row=5, column=0, ipadx=4, pady=4)
button_0.grid(row=5, column=1, ipadx=4, pady=4)
button_point.grid(row=5, column=2, ipadx=4, pady=4)

info_lab1 = tk.Label(root, text="Github: @Phrase-1\nvoice by 音枝優日", width=32, height=2, justify='left', background='#fff0f5', anchor='c')
info_lab1.grid(row=6, column=0, columnspan=4)

# 拦截关闭事件
root.protocol('WM_DELETE_WINDOW', close_window)
# 消息循环
root.mainloop()  # 一直显示
