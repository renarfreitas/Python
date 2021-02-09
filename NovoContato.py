from tkinter import *
import os
import Banco

print(x)

#=============================Criando*funçõe===================================#
def gravarDados():
  if tb_nome.get() != "":
    vnome = tb_nome.get()
    vfone = tb_fone.get()
    vemail = tb_email.get()
    vobs = tb_obs.get("1.0", END)
    vquery = "INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO, T_OBS) VALUES ('"+vnome+"','"+vfone+"','"+vemail+"','"+vobs+"')"
    Banco.dml(vquery)
    tb_nome.delete(0,END)
    tb_fone.delete(0,END)
    tb_email.delete(0,END)
    tb_obs.delete("1.0",END)
    print("Dados Gravados")
  else:
    print("ERROR")
#===========================Criando*a*Janela===================================#
software = Tk()
software.title("CFB Cursos")
software.geometry("500x300")
software.configure(bg = "#dde")

#=====================Criando*elementos*na*Janela==============================#
vbg = "#dde"
vfg = "#009"

#anchor => N = Norte, S = Sul, E = Leste, W - Oeste
#NE = Nordeste, SE = Sudeste, SO = Sudoeste, NO = Noroeste

Label(software, text = "Nome", bg =vbg, fg = vfg, anchor = W).place(x = 10, y = 10, width = 100, height = 20)
tb_nome = Entry(software)
tb_nome.place( x = 10, y = 30, width = 200, height = 20)

Label(software, text = "Telefone", bg =vbg, fg = vfg, anchor = W).place(x = 10, y = 60, width = 100, height = 20)
tb_fone = Entry(software)
tb_fone.place( x = 10, y = 80, width = 100, height = 20)

Label(software, text = "E-mail", bg =vbg, fg = vfg, anchor = W).place(x = 10, y = 110, width = 100, height = 20)
tb_email = Entry(software)
tb_email.place( x = 10, y = 130, width = 300, height = 20)

Label(software, text = "Obs*", bg =vbg, fg = vfg, anchor = W).place(x = 10, y = 160, width = 100, height = 20)
tb_obs = Text(software)
tb_obs.place( x = 10, y = 180, width = 300, height = 80)

btn = Button(software, text = "Gravar", command = gravarDados)
btn.place( x = 10, y = 270, width = 100, height = 20)

#==========================Encerrando*a*Janela=================================#
software.mainloop()