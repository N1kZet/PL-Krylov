import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


root = tk.Tk()
notebook = ttk.Notebook(root)
text_frame = tk.Frame(notebook)     # Фрейм для текстового поля

root.title("Krylov N.")
root.geometry("500x400")
root.resizable(True, True)

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
  num1 = int(num1_entry.get())
  num2 = int(num2_entry.get())
  operator = operator_combobox.get()
  if operator=='+':
    calculate_button["text"] = f"Результат: {num1 +num2}"
  if operator=='-':
    calculate_button["text"] = f"Результат: {num1-num2}"
  if operator=='*':
    calculate_button["text"] = f"Результат: {num1*num2}"
  if operator == '/':
    calculate_button["text"] = f"Результат: {num1/num2}"
calculate_button = tk.Button(calc_tab, text="Вычислить", command=calculate)
calculate_button.grid(row=2, column=1)


checkbox_tab = tk.Frame(notebook)
notebook.add(checkbox_tab, text="Чекбоксы")
# Создание  чекбоксов
def clicked():
    a = selector.get()
    if   a == 1:messagebox.showinfo('Ты выбрал', 'Вариант №1')
    elif a == 2:messagebox.showinfo('Ты выбрал', 'Вариант №2')
    elif a == 3:messagebox.showinfo('Ты выбрал', 'Вариант №3')

selector = IntVar()#область хранения значения для rad_button

rad_button_1 = Radiobutton(checkbox_tab, text='Вариант №1', value=1, variable=selector)
rad_button_1.grid(row=1, column=1)

rad_button_2 = Radiobutton(checkbox_tab, text='Вариант №2', value=2, variable=selector)
rad_button_2.grid(row=1, column=2)

rad_button_3 = Radiobutton(checkbox_tab, text='Вариант №3', value=3, variable=selector)
rad_button_3.grid(row=1, column=3)

vibor = Button(checkbox_tab, text='Что я выбрал?', command=clicked)
vibor.grid(row=1, column=4)

notebook.add(text_frame, text="Текст")
text_editor = Text(text_frame)
text_editor.pack(fill=BOTH, expand=True) # Занимает все доступное пространство

# открываем файл в текстовое поле
def open_file():
  filepath = filedialog.askopenfilename()
  if filepath != "":
    with open(filepath, "r") as file:
      text = file.read()
      text_editor.delete("1.0", END)
      text_editor.insert("1.0", text)

# сохраняем текст из текстового поля в файл
def save_file():
  filepath = filedialog.asksaveasfilename()
  if filepath != "":
    text = text_editor.get("1.0", END)
    with open(filepath, "w") as file:
      file.write(text)

open_button = ttk.Button(text_editor,text="Открыть файл", command=open_file)
open_button.pack(side=LEFT, fill=X, expand=True, padx=10,anchor=SW) # Растягивается по ширине

save_button = ttk.Button(text_editor,text="Сохранить файл", command=save_file)
save_button.pack(side=RIGHT, fill=X, expand=True, padx=10,anchor=SE) # Растягивается по ширине

root.mainloop()
