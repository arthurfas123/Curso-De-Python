class Cubo:
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self, lado):
        self.lado = lado

    def retornarLado(self):
        return print(self.lado)

    def calcularArea(self):
        area = self.lado * self.lado
        return print(area)

cubo = Cubo(2)
cubo.retornarLado()
cubo.mudarLado(3)
cubo.retornarLado()
cubo.calcularArea()
