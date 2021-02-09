from tkinter import *
import os

#===========================Criando*a*Janela===================================#
software = Tk()
software.title("CFB Cursos")
software.geometry("500x300")
software.configure(bg = "#dde")

#=============================Criando*arquivo==================================#
c = os.path.dirname(__file__)
nomeArquivo = c + "\\nomes.txt"

#=============================Criando*funçõe===================================#
def gravarDados():
  arquivo = open(nomeArquivo, "a")
  arquivo.write("Nome......:%s" % vnome.get())
  arquivo.write("\nTelefone:%s" % vfone.get())
  arquivo.write("\nE-mail..:%s" % vemail.get())
  arquivo.write("\nObs.....:%s" % vobs.get("1.0", END))
  arquivo.write("\n")
  arquivo.close()

#=====================Criando*elementos*na*Janela==============================#
vbg = "#dde"
vfg = "#009"

#anchor => N = Norte, S = Sul, E = Leste, W - Oeste
#NE = Nordeste, SE = Sudeste, SO = Sudoeste, NO = Noroeste

Label(software, text = "Nome", bg =vbg, fg = vfg, anchor = W).place(x = 10, y = 10, width = 100, height = 20)
vnome = Entry(software)
vnome.place( x = 10, y = 30, width = 200, height = 20)

Label(software, text = "Telefone", bg =vbg, fg = vfg, anchor = W).place(x = 10, y = 60, width = 100, height = 20)
vfone = Entry(software)
vfone.place( x = 10, y = 80, width = 100, height = 20)

Label(software, text = "E-mail", bg =vbg, fg = vfg, anchor = W).place(x = 10, y = 110, width = 100, height = 20)
vemail = Entry(software)
vemail.place( x = 10, y = 130, width = 300, height = 20)

Label(software, text = "Obs*", bg =vbg, fg = vfg, anchor = W).place(x = 10, y = 160, width = 100, height = 20)
vobs = Text(software)
vobs.place( x = 10, y = 180, width = 300, height = 80)

btn = Button(software, text = "Gravar", command = gravarDados)
btn.place( x = 10, y = 270, width = 100, height = 20)

#==========================Encerrando*a*Janela=================================#
software.mainloop()