import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = tk.Tk()     
notebook = ttk.Notebook(root)
text_frame = tk.Frame(notebook)     # Фрейм для текстового поля

root.title("Krylov N.")    
root.geometry("400x500")
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
operators = ["+", "-", "", "/"]
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
  if operator=='':
    calculate_button["text"] = f"Результат: {num1*num2}"
  if operator == '/':
    calculate_button["text"] = f"Результат: {num1/num2}"
calculate_button = tk.Button(calc_tab, text="Вычислить", command=calculate)
calculate_button.grid(row=2, column=1)


checkbox_tab = tk.Frame(notebook)
notebook.add(checkbox_tab, text="Чекбоксы")
# Создание  чекбоксов

def choose():
  result = "Выбрано: "
  if enavled1.get() == 1: result = f"{result} Первый"
  if enavled2.get() == 1: result = f"{result} Второй"
  if enavled3.get() == 1: result = f"{result} Третий"
  languages.set(result)
    
position = {"padx":4, "pady":4,"expand": True, "anchor":SW}
 
languages = StringVar()
languages_label = ttk.Label(textvariable=languages)
languages_label.pack(position)    


enavled1 = BooleanVar()
checkbox1 = ttk.Checkbutton(checkbox_tab, text="Первый",variable=enavled1, command=choose)
checkbox1.pack(position)

enavled2 = BooleanVar()
checkbox2 = ttk.Checkbutton(checkbox_tab, text="Второй",variable=enavled2, command=choose)
checkbox2.pack(position)

enavled3 = BooleanVar()
checkbox3 = ttk.Checkbutton(checkbox_tab, text="Третий",variable=enavled3, command=choose)
checkbox3.pack(position)


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

open_button = ttk.Button(text="Открыть файл", command=open_file)
open_button.pack(side=LEFT, fill=X, expand=True, padx=10) # Растягивается по ширине

save_button = ttk.Button(text="Сохранить файл", command=save_file)
save_button.pack(side=RIGHT, fill=X, expand=True, padx=10) # Растягивается по ширине

root.mainloop()
