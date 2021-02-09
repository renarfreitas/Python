#===================Inicio===================#
import re
import os

arquivo = "data.txt"
caminho = "C:/Python36-32/Aula/"

if os.path.exists(caminho + arquivo):
  print("Arquivo exitente")
else:
  file = open(caminho + arquivo, "x")
  file.close()
  print("Arquivo Criado")
if os.path.exists(caminho + arquivo):
  os.remove(caminho + arquivo)
  print("Arquivo removido")
else:
  print("Arquivo inexistente")