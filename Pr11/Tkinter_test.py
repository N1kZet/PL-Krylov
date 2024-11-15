import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.title("Krylov N.R.")
notebook = ttk.Notebook(root)

# Создание  фрейма  "Чекбоксы"
checkbox_tab = tk.Frame(notebook)
notebook.add(checkbox_tab, text="Чекбоксы")

# Создание  чекбоксов
checkbox1 = tk.Checkbutton(checkbox_tab, text="Первый")
checkbox1.grid(row=0, column=0)
checkbox2 = tk.Checkbutton(checkbox_tab, text="Второй")
checkbox2.grid(row=1, column=0)
checkbox3 = tk.Checkbutton(checkbox_tab, text="Третий")
checkbox3.grid(row=2, column=0)

# Создание  кнопки  "Выбрать"
def choose():
  # Получение  значений  чекбоксов
  # ...
    pass
  # Вывод  сообщения  с  информацией  о  выборе
  # ...

choose_button = tk.Button(checkbox_tab, text="Выбрать", command=choose)
choose_button.grid(row=3, column=0)

notebook.pack(expand=True, fill="both")
calc_tab = tk.Frame(notebook)
notebook.add(calc_tab, text="Калькулятор")

# Создание  полей  ввода
num1_entry = tk.Entry(calc_tab, width=10)
num1_entry.grid(row=0, column=0)
num2_entry = tk.Entry(calc_tab, width=10)
num2_entry.grid(row=0, column=2)

# Создание  выпадающего  списка  операций
operators = ["+", "-", "*", "/"]
operator_combobox = ttk.Combobox(calc_tab, values=operators)
operator_combobox.grid(row=1, column=1)

# Создание  кнопки  "Вычислить"
def calculate():
  # Получение  значений  из  полей  ввода  и  оператора
  num1 = float(num1_entry.get())
  num2 = float(num2_entry.get())
  operator = operator_combobox.get()

calculate_button = tk.Button(calc_tab, text="Вычислить", command=calculate)
calculate_button.grid(row=2, column=1)

# Создание  фрейма  "Текст"
text_tab = tk.Frame(notebook)
notebook.add(text_tab, text="Текст")

# Создание  поля  ввода  текста
text_area = tk.Text(text_tab, height=10, width=40)
text_area.pack()

# Функция  открытия  файла
def open_file():
  # Открытие  файла  с  помощью  `filedialog.askopenfilename()`
  # ...
    pass
  # Загрузка  текста  из  файла  в  поле  ввода  текста
  # ...

# Создание  меню
menubar = tk.Menu(text_tab)
root.config(menu=menubar)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Файл", menu=filemenu)
filemenu.add_command(label="Открыть", command=open_file)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=root.quit)


root.mainloop()
