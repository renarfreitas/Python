#POO - Classes / P1 - Curso de Python #23
class Carro:
    velMax = 0
    ligado = False
    cor = ""

c1 = Carro()
c2 = Carro()
c3 = Carro()

c1.velMax = 200
c1.cor = "Preto"
c1.ligado = False

print("Velocidade Maxíma: " + str(c1.velMax))
print("Cor: " + c1.cor)
estado = "Y" if c1.ligado else "N"
print("Ligado: " + estado)