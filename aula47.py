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
  #===============Criar Tabela==========================#
vsql="""CREATE TABLE tb_contatos(
            N_IDCONTAO INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOMECONTATO VARCHAR(30),
            T_TELEFONECONTATO VARCHAR(14),
            T_EMAILCONTATO VARCHAR(30)
        );"""
def criarTabela(conexao,sql):
  try:
    c=conexao.cursor()
    c.execute(sql)
    print("Tabela criada")
  except Error as ex:
    print(ex)

criarTabela(vcon,vsql)

vcon.close()