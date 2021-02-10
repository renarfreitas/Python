from tkinter import *
from tkinter import messagebox

def mostrarMsg(tiposmg, msg):
  if(tiposmg == "1"):
    messagebox.showinfo(title = "CFB Cursos", message = msg)
  elif(tiposmg == "2"):
    messagebox.showwarning(title = "CFB Cursos", message = msg)
  elif(tiposmg == "3"):
    messagebox.showerror(title = "CFB Cursos", message = msg)

def resetarTB():
  res = messagebox.askyesno("Resertar", "Confirma reset do textobos?")
  #askyesno / askquestion - SIM e NÃO (True or False)
  #askokcancel - OK e CANCELAR (True or False)
  #askretrycancel - REPETIR e CANCELAR (True or False)
  #askyesnocancel - SIM, NÃO e CANCELAR (True, False E None)
  if (res == True):
    tb_num.delete(0, END)
    tb_num.insert(0, "1")

vmsg = "Curso de Python/Tkinter"

softw = Tk()
softw.title("CFB Cursos")
softw.geometry("500x300")

vnum_cstexto = StringVar()

Label(softw, text = "Tipo de cx(1,2 ou 3)").pack()
tb_num = Entry(softw, textvariable = vnum_cstexto)
vnum_cstexto.set("1")
tb_num.pack()

btn_msg = Button(softw, text = "Mostrar mensagem", command = lambda: mostrarMsg(vnum_cstexto.get(), vmsg))
btn_msg.pack()

btn_reset = Button(softw, text = "Resetar Textbox", command = resetarTB)
btn_reset.pack()

softw.mainloop()