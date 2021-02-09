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

nome = input("Digite o nome: ")
telefone = input("Digite o telefone: ")
email = input("Digite o e-mail: ")

#=================Inserir registro no bd===============#
vsql="INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES('"+nome+"', '"+telefone+"', '"+email+"')"
def inserir(conexao, sql):
  try:
      c=conexao.cursor()
      c.execute(sql)
      conexao.commit()
      print("Registro Inserido")
  except Error as ex:
    print(ex)

inserir(vcon, vsql)