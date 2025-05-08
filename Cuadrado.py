from Color import Color
from FiguraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado=0, color=None):
        FiguraGeometrica.__init__(self, ancho=lado, alto=lado)
        Color.__init__(self,color=color)
    def area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'Cuadrado -> {self.__dict__.__str__()}'

if __name__ == '__main__':
    c1 = Cuadrado(lado=6, color= 'Rojo')
    print(c1)

