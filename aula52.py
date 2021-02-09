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

#=============Consulta no BD===================================#

def consulta(conexao, sql):
  c=conexao.cursor()
  c.execute(sql)
  resultado=c.fetchall()
  return resultado

vsql="SELECT * FROM tb_contatos"
res =  consulta(vcon, vsql)

for r in res:
  print(r)