from tkinter import *
from tkinter import messagebox

def mostrarMsg():
    messagebox.showinfo(title = "CFB Cursos", message = "CFB Cursos, Curso de Python/Tkinter")

softw = Tk()
softw.title("CFB Cursos")
softw.geometry("500x300")

vnum_cstexto = StringVar()

fr_quadro1 = Frame(softw, borderwidth = 1, relief = "solid")
#possíveis valores para o relief = flat, raised, sunken, solid  
fr_quadro1.place(x = 10, y = 10, width = 300, height = 100)

lb_tipo = Label(fr_quadro1, text = "Tipo de cx(1,2 ou 3)")
lb_tipo.place(x = 10, y = 10)
tb_num = Entry(fr_quadro1, textvariable = vnum_cstexto)
vnum_cstexto.set("1")
tb_num.place(x = 10, y = 30)

btn_msg = Button(fr_quadro1, text = "Mostrar mensagem", command = mostrarMsg)
btn_msg.place(x = 10, y = 50)

fr_quadro2 = Frame(softw, borderwidth = 1, relief = "solid", background = "#008")
#possíveis valores para o relief = flat, raised, sunken, solid  
fr_quadro2.place(x = 10, y = 120, width = 300, height = 100)

lb_canal = Label(fr_quadro2, text="CFB Cursos", background = "#008", foreground = "#fff", font = ("Arial", 25))
lb_canal.pack(side = LEFT, fill = X, expand = TRUE)

softw.mainloop()