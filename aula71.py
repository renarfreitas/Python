from tkinter import *
from tkinter import ttk

def imprimirEsporte():
  vesporte = cb_esportes.get()
  print("Esporte " + vesporte)

app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")

listaEsportes =["Futebol", "Vôlei", "Basquete"]

lb_esportes =Label(app, text = "Esportes")
lb_esportes.pack()

cb_esportes = ttk.Combobox(app, values = listaEsportes)
cb_esportes.set("Futebol")
cb_esportes.pack()

btn_esporte = Button(app, text = "Esporte Selecionado", command = imprimirEsporte)
btn_esporte.pack()
app.mainloop()