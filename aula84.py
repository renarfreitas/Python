from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os
def mp(mm):
      return mm/0.352777

pastaApp = os.path.dirname(__file__)

def criarPDF():
      try:
        cnv = canvas.Canvas(pastaApp + "\\cfbcursos.pdf", pagesize = A4)
        cnv.drawImage(pastaApp + "\\grupo-ccr.png", mp(0),mp(270))
        cnv.drawString(mp(100), mp(100), "CFB Cursos")
        cnv.save()
      except:
        messagebox.showinfo(title = "ERRO", message = "Erro ao criar arquivo PDF")
        return
      
      messagebox.showinfo(title = "PDF", message = "PDF Criado")
app = Tk()
app.title("CFB Cursos")
app.geometry("600x450")

btn_criarPDF = Button(app, text = "Criar PDF", command = criarPDF)
btn_criarPDF.pack(side = "left", padx = 10)

app.mainloop()