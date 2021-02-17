import sqlite3
from sqlite3 import Error
import os


pastaapp = os.path.dirname (__file__)
nomeBanco = pastaapp + "\contatos.db"

def conexaoBanco():
  con = None
  try:
    con = sqlite3.connect(nomeBanco)
  except Error as ex:
    print(ex)
  return con

def dql(query): #select
  vcon = conexaoBanco()
  c = vcon. cursor()
  c.execute(query)
  res = c.fetchall()
  vcon.close()
  return res

def dml(query): #insert, update, delete
  try:
    vcon = conexaoBanco()
    c = vcon. cursor()
    c.execute(query)
    vcon.commit()
    vcon.close()
  except Error as ex:
    print(ex)