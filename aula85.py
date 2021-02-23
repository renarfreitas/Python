#Usando a biblioteca urllib para capturar informações de um determinado pg web
import urllib.request

pagina = urllib.request.urlopen("file:///C:/Aulas/Python/Aula85/modelocursopython.html")
texto = pagina.read().decode("utf8")

produto_pos_ini = texto.find("Mouse")
produto_pos_fim = produto_pos_ini + 5

qtde_pos_ini = produto_pos_ini + 14
qtde_pos_fim = qtde_pos_ini + 3

preco_pos_ini = qtde_pos_ini + 12
preco_pos_fim = preco_pos_ini + 7

preco = texto[produto_pos_ini + 26: produto_pos_ini + 26 + 7]

produto = texto[produto_pos_ini:produto_pos_fim]
qtde = texto[qtde_pos_ini:qtde_pos_fim]
preco = texto[preco_pos_ini:preco_pos_fim]

print("Produto....: " + produto)
print("Quantidade.: " + qtde)
print("Preço......: " + preco)
print("\n")