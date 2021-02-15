#Abas e Notebook!
from tkinter import *
from tkinter import ttk

app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")

nb = ttk.Notebook(app,)
nb.place(x = 0, y = 0, width = 500, height = 300)

tb1 = Frame(nb)
nb.add(tb1, text = "Cursos")

lb1 = Label(tb1, text = "Curso de Python")
lb1.pack()

lb2 = Label(tb1, text = "Curso de React Native")
lb2.pack()


tb2 = Frame(nb)
nb.add(tb2, text = "Canal")

lb1 = Label(tb2, text = "youtube.com/cfbcursos")
lb1.pack()


app.mainloop() 