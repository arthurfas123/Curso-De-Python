class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        print(self.cor)

bola = Bola('azul', 3, 'madeira')
bola.mostraCor()
bola.trocaCor('amarelo')
bola.mostraCor()
