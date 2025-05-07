from FiguraGeometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica):
    def __init__(self, alto: float, ancho: float):
        super().__init__(alto, ancho)

    def area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'Rectángulo -> Alto: {self._alto}, Ancho: {self._ancho}, Área: {self.area()}'
    