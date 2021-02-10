from tkinter import *
import os
#import Banco

#===========================Criando*a*Janela===================================#
verify = Tk()
verify.title("Verify - to establish the truth in TI.")
verify.geometry("500x300")
verify.configure(bg = "#dde")

#=============================Criando*funçõe===================================#
def gravarDados():
  if tb_pathost.get() != "":
    vpathost = tb_pathost.get()
    vpatmonitor = tb_patmonitor.get()
    vmatricula = tb_matricula.get()
    vlocaliza = tb_localiza.get()
    vobs = tb_obs.get("1.0", END)
    vquery = "INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO, T_LOCALIZA, T_OBS) VALUES ('"+vpathost+"','"+vpatmonitor+"','"+vmatricula+"','"+vlocaliza+"','"+vobs+"')"
    Banco.dml(vquery)
    tb_pathost.delete(0,END)
    tb_patmonitor.delete(0,END)
    tb_matricula.delete(0,END)
    tb_localiza.delete(0,END)
    tb_obs.delete("1.0",END)
    print("Dados Gravados")
  else:
    print("ERROR")

#=====================Criando*elementos*na*Janela==============================#
vbg = "#dde"
vfg = "#009"

#anchor => N = Norte, S = Sul, E = Leste, W - Oeste
#NE = Nordeste, SE = Sudeste, SO = Sudoeste, NO = Noroeste

Label(verify, text = "Patrimônio do Host", bg =vbg, fg = vfg, anchor = W).place(x = 10, y = 10, width = 200, height = 20)
tb_pathost = Entry(verify)
tb_pathost.place( x = 10, y = 30, width = 120, height = 20)

Label(verify, text = "Patrimônio do Monitor", bg =vbg, fg = vfg, anchor = W).place(x = 10, y = 60, width = 200, height = 20)
tb_patmonitor = Entry(verify)
tb_patmonitor.place( x = 10, y = 80, width = 120, height = 20)

Label(verify, text = "Matricula", bg =vbg, fg = vfg, anchor = W).place(x = 10, y = 110, width = 100, height = 20)
tb_matricula = Entry(verify)
tb_matricula.place( x = 10, y = 130, width = 120, height = 20)

Label(verify, text = "Localização", bg =vbg, fg = vfg, anchor = W).place(x = 10, y = 160, width = 100, height = 20)
tb_localiza = Entry(verify)
tb_localiza.place( x = 10, y = 180, width = 300, height = 20)

Label(verify, text = "Obs*", bg =vbg, fg = vfg, anchor = W).place(x = 10, y = 210, width = 100, height = 20)
tb_obs = Text(verify)
tb_obs.place( x = 10, y = 230, width = 300, height = 40)

btn = Button(verify, text = "Gravar", command = gravarDados)
btn.place( x = 10, y = 275, width = 100, height = 20)

#==========================Encerrando*a*Janela=================================#
verify.mainloop()
