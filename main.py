from tkinter import *

root = Tk()
root.title("Python ticket price calculator")
root.geometry('600x600')

canvas = Canvas(root, width=600, height=600, bg='#002')

#grid v
for y in range(21):
    k = 50*y
    canvas.create_line(10+k, 610, 10+k, 10, width=1, fill='#191938')

#grid h
for x in range(13):
    k = 50*x
    canvas.create_line(10, 10+k, 1010, 10+k, width=1, fill='#191938')

# enter field
entry_number = Entry(root, width=70, bg='black', fg='green', justify='center')
entry_number.place(x=10, y=10)

# enter field (rez 1)
label_rez = Label(root, text= 'Три', bg='black', fg='yellow')
label_rez.place(x=10, y=150)

# текстовое поле вывода (результата 2)
label_rez_2 = Label(root, text= 'Пять', bg='black', fg='yellow')             # вывода результата
label_rez_2.place(x=10, y=200)                      # расположение текстового поля результата

# текстовое поле вывода (результата 3)
label_rez_3 = Label(root, text= 'Пять и пять', bg='black', fg='yellow')      # вывода результата
label_rez_3.place(x=10, y=250)                      # расположение текстового поля результата

# текстовое поле вывода (результата 4)
label_rez_4 = Label(root, text= 'Шесть', bg='black', fg='yellow')            # вывода результата
label_rez_4.place(x=10, y=300)                      # расположение текстового поля результата

# текстовое поле вывода (результата 5)
label_rez_5 = Label(root, text= 'Шесть и пять', bg='black', fg='yellow')     # вывода результата
label_rez_5.place(x=10, y=350)                      # расположение текстового поля результата

# текстовое поле вывода (результата 6)
label_rez_6 = Label(root, text= 'Десять', bg='black', fg='yellow')           # вывода результата
label_rez_6.place(x=10, y=400)                      # расположение текстового поля результата

# текстовое поле вывода (результата 7)
label_rez_7 = Label(root, text= 'Одиннадцать', bg='black', fg='yellow')      # вывода результата
label_rez_7.place(x=10, y=450)                      # расположение текстового поля результата

# текстовое поле вывода (результата 8)
label_rez_8 = Label(root, text= 'Двенадцать', bg='black', fg='yellow')       # вывода результата
label_rez_8.place(x=10, y=500)                      # расположение текстового поля результата

# текстовое поле суммы.
label_rez_rez = Label(root, text= 'Результат', bg='blue', fg='white')          # вывода результата
label_rez_rez.place(x=10, y=550)                        # расположение текстового поля результата

def calc():
    rez = entry_number.get().split(" ")

    n = 'кол-во:'
    sum = ' сумма:'

    rez_3 = rez.count('3')
    rez_3_sum = int(rez.count('3')) * 3
    arr = ('3 грн ', n, rez_3, sum, rez_3_sum)
    def f_3():
        return arr[0], arr[1], arr[2], arr[3], arr[4]
    label_rez['text'] = f_3()

    rez_5 = rez.count('5')
    rez_5_sum = int(rez.count('5')) * 5
    arr = ('5 грн ', n, rez_5, sum, rez_5_sum)
    def f_5():
        return arr[0], arr[1], arr[2], arr[3], arr[4]
    label_rez_2['text'] = f_5()

    rez_5_5 = rez.count('5.5')
    rez_5_5_sum = int(rez.count('5.5')) * 5.5
    arr = ('5.5 грн ', n, rez_5_5, sum, rez_5_5_sum)
    def f_5_5():
        return arr[0], arr[1], arr[2], arr[3], arr[4]
    label_rez_3['text'] = f_5_5()

    rez_6 = rez.count('6')
    rez_6_sum = int(rez.count('6')) * 6
    arr = ('6 грн ', n, rez_6, sum, rez_6_sum)
    def f_6():
        return arr[0], arr[1], arr[2], arr[3], arr[4]
    label_rez_4['text'] = f_6()

    rez_6_5 = rez.count('6.5')
    rez_6_5_sum = int(rez.count('6.5')) * 6.5
    arr = ('6.5 грн ', n, rez_6_5, sum, rez_6_5_sum)
    def f_6_5():
        return arr[0], arr[1], arr[2], arr[3], arr[4]
    label_rez_5['text'] = f_6_5()

    rez_10 = rez.count('10')
    rez_10_sum = int(rez.count('10')) * 10
    arr = ('10 грн ', n, rez_10, sum, rez_10_sum)
    def f_10():
        return arr[0], arr[1], arr[2], arr[3], arr[4]
    label_rez_6['text'] = f_10()

    rez_11 = rez.count('11')
    rez_11_sum = int(rez.count('11')) * 11
    arr = ('11 грн ', n, rez_11, sum, rez_11_sum)
    def f_11():
        return arr[0], arr[1], arr[2], arr[3], arr[4]
    label_rez_7['text'] = f_11()

    rez_12 = rez.count('12')
    rez_12_sum = int(rez.count('12')) * 12
    arr = ('12 грн ', n, rez_12, sum, rez_12_sum)
    def f_12():
        return arr[0], arr[1], arr[2], arr[3], arr[4]
    label_rez_8['text'] = f_12()

# результат общий функция суммирующая общую сумму
    def f_rez_rez():
        return int(rez_3_sum) + int(rez_5_sum) + int(rez_5_5_sum) + int(rez_6_sum) + int(rez_6_5_sum) + int(rez_10_sum) + int(rez_11_sum) + int(rez_12_sum)
    label_rez_rez['text'] = f_rez_rez()

# создание кнопки
btn = Button(
    root, 
    text='Submit', 
    background="red", 
    foreground="#ccc", 
    padx="20", 
    pady="10", 
    font="10")

btn.bind('<Button-1>', lambda event: calc())       # реакция на л.к.м
btn.place(x=470, y=70)                             # расположение кнопки

# кнопка с функцией 3
def fn_btn_3():
    entry_number.insert(END, "3 ")

btn_3 = Button(root, text='3', background="blue", foreground="#ccc", padx="5", pady="10", font="10")
btn_3.bind('<Button-1>', lambda event: fn_btn_3())
btn_3.place(x=10, y=70)

# кнопка с функцией 5
def fn_btn_5():
    entry_number.insert(END, "5 ")

btn_5 = Button(root, text='5', background="blue", foreground="#ccc", padx="5", pady="10", font="10")
btn_5.bind('<Button-1>', lambda event: fn_btn_5())
btn_5.place(x=50, y=70) 

# кнопка с функцией 5.5
def fn_btn_5_5():
    entry_number.insert(END, "5.5 ")

btn_5 = Button(root, text='5.5', background="blue", foreground="#ccc", padx="5", pady="10", font="10")
btn_5.bind('<Button-1>', lambda event: fn_btn_5_5())
btn_5.place(x=90, y=70)

# кнопка с функцией 6
def fn_btn_6():
    entry_number.insert(END, "6 ")

btn_6 = Button(root, text='6', background="blue", foreground="#ccc", padx="5", pady="10", font="10")
btn_6.bind('<Button-1>', lambda event: fn_btn_6())
btn_6.place(x=150, y=70)

# кнопка с функцией 6.5
def fn_btn_6_5():
    entry_number.insert(END, "6.5 ")

btn_6_5 = Button(root, text='6.5', background="blue", foreground="#ccc", padx="5", pady="10", font="10")
btn_6_5.bind('<Button-1>', lambda event: fn_btn_6_5())
btn_6_5.place(x=200, y=70)

# кнопка с функцией 10
def fn_btn_10():
    entry_number.insert(END, "10 ")

btn_10 = Button(root, text='10', background="blue", foreground="#ccc", padx="5", pady="10", font="10")
btn_10.bind('<Button-1>', lambda event: fn_btn_10())
btn_10.place(x=260, y=70)

# кнопка с функцией 11
def fn_btn_11():
    entry_number.insert(END, "11 ")

btn_11 = Button(root, text='11', background="blue", foreground="#ccc", padx="5", pady="10", font="10")
btn_11.bind('<Button-1>', lambda event: fn_btn_11())
btn_11.place(x=310, y=70)

# кнопка с функцией 12
def fn_btn_12():
    entry_number.insert(END, "12 ")

btn_12 = Button(root, text='12', background="blue", foreground="#ccc", padx="5", pady="10", font="10")
btn_12.bind('<Button-1>', lambda event: fn_btn_12())
btn_12.place(x=370, y=70)


canvas.pack()
root.mainloop()
