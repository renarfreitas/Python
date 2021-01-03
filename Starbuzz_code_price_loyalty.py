import urllib.request #modulo que dá ao programa a capacidade de conversar com uma pagina na web#

page = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html") #Atribui a uma variavel a pagina web desejada#
text = page.read().decode("utf8") #Converte a pagina web bruta em um texto legivel#
price = text[249:255]

#métodos de pesquisa em uma string ou substring#
valor = text.find(">$")
valor1 = text.endswith(">$")
valor2 = text.startswith(">$")
valor3 = text.strip()

print(price)
print(valor)
print(valor1)
print(valor2)
print(valor3)
print(text)

