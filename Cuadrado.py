from FiguraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado: float):
        super().__init__(lado, lado)

    def area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'Cuadrado -> Alto: {self._alto}, Ancho: {self._ancho}, Área: {self.area()}'
