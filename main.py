import tkinter as tk
from random import choice
from tkinter import messagebox

# Список ідей
ideas = [
    "Написать книгу",
    "Начать бегать по утрам",
    "Создать свой блог",
    "Выучить новый язык",
    "Попробовать рисовать",
    "Сходить в поход",
    "Изучить программирование",
    "Почитать интересную книгу",
    "Путешествовать в новую страну"
]

# Функция для генерации случайной идеи
def generate_idea():
    if ideas:
        idea = choice(ideas)
        messagebox.showinfo("Ваша идея", idea)
    else:
        messagebox.showwarning("Нет идей", "Идеи закончились!")

# Основное окно
window = tk.Tk()
window.resizable(width=False, height=False)
window.title("Генератор идей")
window.geometry("720x360")

# Текст приветствия
greeting_label = tk.Label(
    window, text="Нажмите на кнопку, чтобы получить идею!", font=("Arial", 16)
)
greeting_label.pack(pady=20)

# Кнопка генерации идеи
generate_button = tk.Button(
    window, text="Сгенерировать идею", font=("Arial", 14), command=generate_idea
)
generate_button.pack(pady=10)

# Запуск приложения
window.mainloop()
