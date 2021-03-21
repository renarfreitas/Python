#POO - Classes / P2 / Construtor e métodos - Curso de Python #24
class Carro:
    velMax = 0
    ligado = False
    cor = ""
    def __init__(self,vm,li,c): #Construtor de Classe
        self.velMax = vm
        self.ligado = li
        self.cor = c
    def viewer(self):
        print("-----------------------------")
        print("Velocidade Maxíma: " + str(self.velMax))
        print("Cor..............: " + self.cor)
        estado = "Y" if self.ligado else "N"
        print("Ligado...........: " + estado)
        print("-----------------------------")
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def mover(self):
        if (self.ligado):
            print("Em movimento...")
        else:
            print("Carro desligado!")


c1 = Carro(200,False, "Black")
c2 = Carro(120, False, "white")
c3 = Carro(350, False, "Red")

c1.ligar()
c2.ligar()

c1.viewer()
c2.viewer()
c3.viewer()

c1.mover()
c2.mover()