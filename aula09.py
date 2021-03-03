#Coleção List
carros = ["HRV", "Golf", "Argo", "Focus"]


#Adicionar items na List
carros.append("Fit")
carros.append("Fusion")
carros.append("Polo")

#Copiar uma List para Outra
carros2 = ["Fusca", "147", "Brasilia", "Celta"]
carros3 = carros+carros2

#Remover items na List
carros.remove("Fusion")

#Remover o ultimo elemento da List
carros.pop()

#Remove um elemento em posição determinada na List
del carros[2]

#Removo ou apaga todos elementos da List
carros.clear()

print(str(len(carros)) + " carros na lista 1")
print(carros, "\n")
print(str(len(carros2)) + " carros na lista 2")
print(carros2, "\n")
print(str(len(carros3)) + " carros na lista 3")
print(carros3)