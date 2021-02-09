from tkinter import *

def imprimirEsporte():
  ve = vesporte.get()
  if ve == "Futebol":
    print("Esporte Futebol")
  elif ve == "Vôlei":
    print("Esporte Vôlei")
  elif ve == "Basquete":
    print("Esporte Basquete")
  else:
    print("Selecione um esporte!")

softw = Tk()
softw.title("CFB Cursos")
softw.geometry("500x300")

listaEsportes = ["Futebol", "Vôlei", "Basquete"]

vesporte = StringVar()
vesporte.set(listaEsportes[0]) #Valor Padrão.

bl_esportes = Label(softw, text = "Esportes")
bl_esportes.pack()

op_esportes = OptionMenu(softw, vesporte, *listaEsportes)
op_esportes.pack()

btn_esporte = Button(softw, text = "Esporte selecionado", command = imprimirEsporte)
btn_esporte.pack()

softw.mainloop()