import urllib.request #Modulo que dá ao programa a capacidade de conversar com uma pagina na web#
import time
#Definindo a função para exibir o preço do grão atual.#
def get_price():
    page = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html") #Atribui a uma variavel a pagina web desejada#
    text = page.read().decode("utf8") #Converte a pagina web bruta em um texto legivel#
    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    return(text[start_of_price:end_of_price])
get_price()
#Definindo a função para enviar menssagem para twitter do cliente.#
def send_to_twitter():
    msg = "I am a message that will be sent to twitter"
    password_manager = urllib.request.HTTPPasswordMgr()
    password_manager.add_password("Twitter API","https://twitter.com", "login...", "Password...")
    http_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
    page_opener = urllib.request.build_opener(http_handler)
    urllib.request.install_opener(page_opener)
    params = urllib.parse.urlencode({'status': msg})
    resp = urllib.request.urlopen("https://twitter.com/statuses/update.json",params)
    resp.read()

print("Welcome to verification price Starbuzz 2.0")
price_now = input("Do you want to see the price now: say Y or N?")
if price_now == "Y":
    send_to_twitter()
else:
    price = 99.99
    while price > 4.74:
        time.sleep(10)
        print (get_price())
        send_to_twitter()
