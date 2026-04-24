import tkinter as tk
import random


git_hub = "https://github.com/xzl1te26-code/random-facts-tkinter"

# Список интересных фактов
facts = [
    "Бананы радиоактивны и излучают небольшое количество гамма-излучения.",
    "Человек может обойтись без пищи до 2 месяцев, а без воды — всего несколько дней.",
    "Голубые киты ежедневно потребляют около 4 тонн пищи.",
    "Пчёлы могут распознавать лица людей.",
    "Существует 6 000 видов бананов, а не только один."
]

def show_random_fact():
    """Функция выбирает случайный факт и обновляет текст в метке"""
    random_fact = random.choice(facts)
    fact_label.config(text=random_fact)

# Настройка главного окна
root = tk.Tk()
root.title("Интересные факты")
root.geometry("400x250")

# Создание текстовой метки для вывода факта
# wraplength позволяет тексту переноситься на новую строку, если он длинный
fact_label = tk.Label(
    root, 
    text="Нажмите на кнопку, чтобы узнать что-то новое!", 
    font=("Arial", 12), 
    wraplength=350, 
    justify="center"
)
fact_label.pack(expand=True, padx=20, pady=20)

# Создание кнопки
btn_show = tk.Button(
    root, 
    text="Показать факт", 
    command=show_random_fact, 
    font=("Arial", 10, "bold"),
    bg="#4caf50", 
    fg="white",
    padx=10,
    pady=5
)
btn_show.pack(pady=20)

# Запуск основного цикла программы
root.mainloop()