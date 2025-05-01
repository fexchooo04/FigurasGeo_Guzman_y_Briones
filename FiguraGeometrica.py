class FiguraGeometrica:
    def __init__(self, alto: float, ancho: float):
        self._alto = alto
        self._ancho = ancho
    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self, value):