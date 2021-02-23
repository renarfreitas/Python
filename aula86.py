#Usando a biblioteca urllib para capturar informações de um determinado pg web
import urllib.request

pagina = urllib.request.urlopen("file:///C:/Aulas/Python/Aula85/modelocursopython.html")
texto = pagina.read().decode("utf8")

produto = input("Digite o produto: ")
produto_pos = texto.find(produto)
produto_txt = texto[produto_pos:100000]
preco_pos = produto_txt.find("R$")
preco = texto[produto_pos + preco_pos:produto_pos + preco_pos + 7]

if (preco_pos > -1):
    print("Produto: " + produto)
    print("Preço: "   + preco)
else:
    print("Produto não encontrado!")