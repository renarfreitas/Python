#Dictionary - Curso de Python #17
carro  = {
    "Fabricante":"Honda",
    "Modelo":"HRV",
    "Ano":"2016",
    "Cor":"Prata"
}
#inserir items ao dicionário
carro["Cor"] = "Preto"
carro["Cambio"] = "Automatico"

#removoer items do dicionário
#carro.pop[]
#del carro[]

print("Tamanho do Dictionary: "+ str(len(carro)))
fab = carro.get("Fabricante") # = fab=carro["Fabricante"]
if "Modelo" in carro:
    print("\n Sim, modelo é uma chave \n")
for c, v in carro.items():
    print(c + " : " + v) #Chave
    #print(carro[x]) #Valor

Carro1={
    "Fabricante":"Honda",
    "Modelo":"HRV"
}
Carro2={
    "Fabricante":"Volkswagem",
    "Modelo":"Golf"
}
Carro3={
    "Fabricante":"Ford",
    "Modelo":"Focus"
}

Carros = {
    "C1":Carro1,
    "C2":Carro2,
    "C2":Carro3
}

print("\n",Carros["C1"]["Fabricante"])