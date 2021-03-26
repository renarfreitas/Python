#Iterators - Curso de Python #29

carros = ["HRV","Polo","Jetta","Cruze","Fusion"]

intCarros = iter(carros)

while intCarros:
    try:
        print(next(intCarros))
    except StopIteration:
        print("Fim da lista")
        break

