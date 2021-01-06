import urllib.request #Modulo que dá ao programa a capacidade de conversar com uma pagina na web#

#Definindo a função para exibir o preço do grão atual.#
def get_price():
    page = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html") #Atribui a uma variavel a pagina web desejada#
    text = page.read().decode("utf8") #Converte a pagina web bruta em um texto legivel#
    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    return(text[start_of_price:end_of_price])
get_price()

discount = 0.9
print("The discount price is: ",discount)
price = float(get_price())
actual_price = price*discount
print(str(actual_price))
