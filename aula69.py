from tkinter import *
import os

def futebolClicado():
  esp = str (vfutebol.get())
  print("Futebol:"+esp)
def voleiClicado():
  esp = str(vvolei.get())
  print("Volei:"+esp)
def basqueteClicado():
  esp = str(vbasquete.get())
  print("Basquete:"+esp)

softw = Tk()
softw.title("CFB Cursos")
softw.geometry("500x300")

vfutebol = StringVar()
vvolei = StringVar()
vbasquete = StringVar()

fr_quadro1 = Frame(softw, borderwidth = 1, relief = "solid")
#relief (flat, raised, sunken, solid)
fr_quadro1.place(x = 10, y = 10, width = 300, height = 100)

cb_futebol = Checkbutton(fr_quadro1, text = "Futebol", variable = vfutebol, onvalue = "s", offvalue = "n", command = futebolClicado)
cb_futebol.pack(side = LEFT)

cb_volei = Checkbutton(fr_quadro1, text = "Volei", variable = vvolei, onvalue = "s", offvalue = "n", command = voleiClicado)
cb_volei.pack(side = LEFT)

cb_basquete = Checkbutton(fr_quadro1, text = "Basquete", variable = vbasquete, onvalue = "s", offvalue = "n", command = basqueteClicado)
cb_basquete.pack(side = LEFT)

softw.mainloop()