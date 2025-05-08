from FiguraGeometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica):
    def __init__(self, alto: float, ancho: float):
        super().__init__(alto, ancho)

    def area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'Rectángulo -> {self.__dict__.__str__()}'
if __name__ == '__main__':
    r1 = Rectangulo(alto=5, ancho=3)
    print(r1)
