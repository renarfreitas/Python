from tkinter import *
import os


def impSenha():
  print("A senha digitaada foi: " +vsenha.get())
 

softw = Tk()
softw.title("CFB Cursos")
softw.geometry("500x300")

vsenha = StringVar()

p_senha = Entry(softw, textvariable = vsenha, show = "#")
p_senha.pack()

btn_mostrarsenha = Button(softw, text = "Imprimir Senha", command = impSenha)
btn_mostrarsenha.pack()



softw.mainloop()