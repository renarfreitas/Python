from tkinter import *
import os

pastaSoftw = os.path.dirname(__file__)

softw = Tk()
softw.title("CFB Cursos")
softw.geometry("500x300")

imgLogo = PhotoImage(file = pastaSoftw+"\\p_CCR_Metrô_Bahia.png")
l_logo =Label(softw, image = imgLogo)
l_logo.place(x = 10, y = 10)

softw.mainloop()