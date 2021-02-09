import sqlite3
from sqlite3 import Error

#=================Criar Conexão com bd==================#
def conexaobd():
  caminho = "C:\\Python36-32\\Aula\\banco\\inventario.db"
  conexao=None
  try:
    conexao=sqlite3.connect(caminho)
  except Error as ex:
    print(ex)
  return conexao

vcon = conexaobd()

#=================Inserir registro no bd - INSERTE===============#

#def inserir(conexao, sql):
#  try:
#      c=conexao.cursor()
#      c.execute(sql)
#      conexao.commit()
#  except Error as ex:
#      print(ex)
#  finally:
#      print("Registro Inserido")

#nome = input("Digite o nome: ")
#telefone = input("Digite o telefone: ")
#email = input("Digite o e-mail: ")
#vsql="INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES('"+nome+"', '"+telefone+"', '"+email+"')"
#inserir(vcon, vsql)

#===================Deletar registro no bd - DELETE===================#

#def deletar(conexao, sql):
#  try:
#    c=conexao.cursor()
#    c.execute(sql)
#    conexao.commit()
#  except Error as ex:
#    print(ex)
#  finally:
#    print("Registro removido")
#vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO = 2"
#deletar(vcon, vsql)