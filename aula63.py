from tkinter import *

softw = Tk()
softw.title("CFB Cursos")
softw.geometry("500x300")

def imprimirEsporte():
  ve = vesporte.get()
  if ve == "f":
    print("Esporte Futebol")
  elif ve == "v":
    print("Esporte Vôlei")
  elif ve == "b":
    print("Esporte Basquete")
  else:
    print("Selecione um esporte!") 

vesporte = StringVar()
vcor = StringVar()

bl_esportes = Label(softw, text = "Esportes")
bl_esportes.pack()

rb_futebol = Radiobutton(softw, text = "Futebol", value = "f", variable = vesporte)
rb_futebol.pack()

rb_volei = Radiobutton(softw, text = "Vôlei", value = "v", variable = vesporte)
rb_volei.pack()

rb_basquete = Radiobutton(softw, text = "Basquete", value = "b", variable = vesporte)
rb_basquete.pack()

rb_verde = Radiobutton(softw, text = "Verde", value = "vd", variable = vcor)
rb_verde.pack()

rb_vermelho = Radiobutton(softw, text = "Vermelho", value = "vm", variable = vcor)
rb_vermelho.pack()

btn_esporte = Button(softw, text = "Esporte selecionado", command = imprimirEsporte)
btn_esporte.pack()

softw.mainloop()