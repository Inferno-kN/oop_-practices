import tkinter



def present():
    name = entry_name.get()
    email1 = entry_email1.get()
    email2 = entry_email2.get()
    sex = entry_sex.get()

run = tkinter.Tk
run.title("Регистрация")

tkinter.Label(run, text="Ваше полное имя >>").pack(pady=5)
entry_name = tkinter.Entry(run)
entry_name.pack(pady=5)

tkinter.Label(run, text="Ваш email1 >>").pack(pady=5)
entry_email1 = tkinter.Entry(run)
entry_email1.pack(pady=5)

tkinter.Label(run, text="Ваш email2 >>").pack(pady=5)
entry_email2 = tkinter.Entry(run)
entry_email2.pack(pady=5)

tkinter.Label(run, text="Ваш пол >>").pack(pady=5)
entry_sex = tkinter.Entry(run)
entry_sex.pack(pady=5)

btn_submit = tkinter.Button(run, text="SUBMIT")
btn_submit.pack(pady=5)


run.mainloop()
