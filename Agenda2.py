from tkinter import *
import os

pastaSfw = os.path.dirname (__file__)

def semComando():
  print("")

def novoContato():
#===========================Abrir*Nova*Janela==================================#
  exec(open(pastaSfw + "\\NovoContato.py").read(), {'x':10})
#===========================Criando*a*Janela===================================#
software = Tk()
software.title("CFB Cursos")
software.geometry("500x300")
software.configure(bg = "#dde")

#=================================Criando*Menu=================================#
barraDeMenus = Menu(software)
menuContatos = Menu(barraDeMenus, tearoff = 0)
menuContatos.add_command(label = "Novo", command = novoContato)
menuContatos.add_command(label = "Pesquisar", command = semComando)
menuContatos.add_command(label = "Deletar", command = semComando)
menuContatos.add_separator()
menuContatos.add_command(label = "Fechar", command = software.quit)
barraDeMenus.add_cascade(label = "Contatos", menu = menuContatos)

menuManutencao = Menu(barraDeMenus, tearoff = 0)
menuManutencao.add_command(label = "Banco de Dados", command = semComando)
barraDeMenus.add_cascade(label = "Manutenção", menu = menuManutencao)

menuSobre = Menu(barraDeMenus, tearoff = 0)
menuSobre.add_command(label = "CFB Cursos", command = semComando)
barraDeMenus.add_cascade(label = "Sobre", menu = menuSobre)


software.config(menu = barraDeMenus)

#==========================Encerrando*a*Janela=================================#
software.mainloop()