import numpy as np
import tkinter as tk
import tkinter.messagebox
from backend import scipy_algo, my_algo


window = tk.Tk()             # Объект окна
window.title("Main Window")  # Имя окна
window.geometry("530x500")   # Размер окна
window.resizable(0, 0)       # Запретить изменение размера окна


# Функция для валидации вводимых символов
def InputValidation(sym: str) -> bool:
    allowedSymbols = ['-', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if sym in allowedSymbols:
        return True
    else:
        window.bell()
        return False


# Упаковка лейблов на окне
tk.Label(text="План производства изделий A и B").grid(row = 1, column = 1, columnspan = 4)
tk.Label(text="Часов на ед. A").grid(row = 2, column = 2)
tk.Label(text="Часов на ед. B").grid(row = 2, column = 3)
tk.Label(text="Всего не более часов").grid(row = 2, column = 4)
tk.Label(text="Тип оборудования I").grid(row = 3, column = 1, sticky='e')
tk.Label(text="Тип оборудования II").grid(row = 4, column = 1, sticky='e')
tk.Label(text="Тип оборудования III").grid(row = 5, column = 1, sticky='e')
tk.Label(text="Прибыль за ед. изделия A").grid(row = 6, column = 1)
tk.Label(text="Прибыль за ед. изделия B").grid(row = 7, column = 1)
tk.Label(text="Решение: ").grid(row = 8, column = 1)
tk.Label(text="Максимум: ").grid(row = 8, column = 3)
lblSolution = tk.Label(text="")
lblSolution.grid(row = 8, column = 2)
lblMaxFun = tk.Label(text="")
lblMaxFun.grid(row = 8, column = 4)


# Упаковка однострочных текстовых полей
vcmd = (window.register(InputValidation), '%S')  # Зарегистрировать событие
# Первая строка
entry11 = tk.Entry(validate='key', validatecommand=vcmd)
entry11.grid(row = 3, column = 2)
entry12 = tk.Entry(validate='key', validatecommand=vcmd)
entry12.grid(row = 3, column = 3)
entry13 = tk.Entry(validate='key', validatecommand=vcmd)
entry13.grid(row = 3, column = 4)
# Вторая строка
entry21 = tk.Entry(validate='key', validatecommand=vcmd)
entry21.grid(row = 4, column = 2)
entry22 = tk.Entry(validate='key', validatecommand=vcmd)
entry22.grid(row = 4, column = 3)
entry23 = tk.Entry(validate='key', validatecommand=vcmd)
entry23.grid(row = 4, column = 4)
# Третья строка
entry31 = tk.Entry(validate='key', validatecommand=vcmd)
entry31.grid(row = 5, column = 2)
entry32 = tk.Entry(validate='key', validatecommand=vcmd)
entry32.grid(row = 5, column = 3)
entry33 = tk.Entry(validate='key', validatecommand=vcmd)
entry33.grid(row = 5, column = 4)
# Ввод прибыли
entryProfitA = tk.Entry(width=60, validate='key', validatecommand=vcmd)
entryProfitA.grid(row = 6, column = 2, columnspan = 3, sticky='e')
entryProfitB = tk.Entry(width=60, validate='key', validatecommand=vcmd)
entryProfitB.grid(row = 7, column = 2, columnspan = 3, sticky='e')


# Обработчик нажатия для первой кнопки
def btnSP_Handler(event):
    try:
        a = [[float(entry11.get()), float(entry12.get())],
            [float(entry21.get()), float(entry22.get())],
            [float(entry31.get()), float(entry32.get())]]
        b = [float(entry13.get()), float(entry23.get()), float(entry33.get())]
        c = [float(entryProfitA.get()), float(entryProfitB.get())]
        solution, max_val = scipy_algo(a, b, c)
        lblSolution["text"] = str(solution)
        lblMaxFun["text"] = str(max_val)
    except ValueError:
        tk.messagebox.showerror(title="Error!", message="Введите правильное число")


# Обработчик нажатия для второй кнопки
def btnMY_Handler(event):
    try:
        a = [[float(entry11.get()), float(entry12.get())],
            [float(entry21.get()), float(entry22.get())],
            [float(entry31.get()), float(entry32.get())]]
        b = [float(entry13.get()), float(entry23.get()), float(entry33.get())]
        c = [float(entryProfitA.get()), float(entryProfitB.get())]
        solution, max_val = my_algo(a, b, c)
        lblSolution["text"] = str(solution)
        lblMaxFun["text"] = str(max_val)
    except ValueError:
        tk.messagebox.showerror(title="Error!", message="Введите правильное число")


# Упаковка кнопок
btnSP = tk.Button(window, text="Рассчёт SciPy", width=60, height=3)
btnSP.grid(row = 9, column = 1, columnspan = 4)
btnSP.bind("<Button-1>", btnSP_Handler)
btnMY = tk.Button(window, text="Рассчёт моего алгоритма", width=60, height=3)
btnMY.grid(row = 10, column = 1, columnspan = 4)
btnMY.bind("<Button-1>", btnMY_Handler)


# Запуск оконного цикла
window.mainloop()
