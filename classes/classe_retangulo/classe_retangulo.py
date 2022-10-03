class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarLado(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def retornarLado(self):
        return self.ladoA, self.ladoB

    def calcularArea(self):
        area = self.ladoA * self.ladoB
        return area

    def perimetro(self):
        perimetro = self.ladoA * 2 + self.ladoB * 2
        return perimetro
