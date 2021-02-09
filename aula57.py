from tkinter import *

software = Tk()
software.title("CFB Cursos")
software.geometry("500x300")
software.configure(background="#008")

vtxt = "Módulo Tkinter"
vbg = "#ff0"
vfg = "#000"

txt1 = Label(software, text = vtxt, bg =vbg, fg = vfg)
txt1.place(x=10, y=10, width=100, height=30)

txt2 = Label(software, text = vtxt, bg =vbg, fg = vfg)
txt2.pack(ipadx = 20, ipady = 20, padx = 5, pady = 5, side = "bottom", fill = Y, expand = True)

software.mainloop()