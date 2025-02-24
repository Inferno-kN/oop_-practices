import customtkinter as tk
from tkinter import messagebox


def input_info():
    name = entry_name.get()
    email = entry_name.get()
    age = entry_age.get

    if not name or not email or not age:
        messagebox.showerror("Ошибка, заполните данные правильно!")

    if age <= 0:
        raise ValueError("Возраст должен быть положительным")
    return

    if "@" not in email:
        messagebox.showerror("В названии почты должен быть символ @")
        return


    messagebox.showinfo("Успешные корректные данные!")

run = ctk.CTk()
run.title("Форма ввода данных")

# Создание виджетов
label_name = ctk.CTkLabel(app, text="Имя:")
label_name.pack(pady=(10, 0))

entry_name = ctk.CTkEntry(app)
entry_name.pack(pady=(0, 10))

label_email = ctk.CTkLabel(app, text="Email:")
label_email.pack(pady=(10, 0))

entry_email = ctk.CTkEntry(app)
entry_email.pack(pady=(0, 10))

label_age = ctk.CTkLabel(app, text="Возраст:")
label_age.pack(pady=(10, 0))

entry_age = ctk.CTkEntry(app)
entry_age.pack(pady=(0, 10))


run.mainloop()

