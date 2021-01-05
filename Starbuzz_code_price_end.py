import urllib.request #modulo que dá ao programa a capacidade de conversar com uma pagina na web#
import time

price = 99.99
while price > 4.74:
    time.sleep(900)
    page = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html") #Atribui a uma variavel a pagina web desejada#
    text = page.read().decode("utf8") #Converte a pagina web bruta em um texto legivel#
    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    price = float(text[start_of_price:end_of_price])

print("Buy!")
