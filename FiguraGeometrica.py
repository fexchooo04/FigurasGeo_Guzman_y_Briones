class FiguraGeometrica:
    def __init__(self, alto: float, ancho: float):
        self._alto = alto
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, nuevo_alto):
        if isinstance(nuevo_alto, (int, float)) and nuevo_alto > 0:
            self._alto = nuevo_alto
        else:
            raise ValueError("El alto debe ser un número positivo.")

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter  # Se corrigió el decorador, antes estaba mal definido como @alto.setter
    def ancho(self, nuevo_ancho):
        if isinstance(nuevo_ancho, (int, float)) and nuevo_ancho > 0:
            self._ancho = nuevo_ancho
        else:
            raise ValueError("El ancho debe ser un número positivo.")

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado: float):
        super().__init__(lado, lado)

    def area(self):
        return self._alto * self._ancho

    def __str__(self):  # Se corrigió el nombre del método de `str` a `__str__`
        return f'Cuadrado -> Alto: {self._alto}, Ancho: {self._ancho}, Área: {self.area()}'

class Rectangulo(FiguraGeometrica):
    def __init__(self, alto: float, ancho: float):
        super().__init__(alto, ancho)

    def area(self):
        return self._alto * self._ancho

    def __str__(self):  # Se corrigió el nombre del método de `str` a `__str__`
        return f'Rectángulo -> Alto: {self._alto}, Ancho: {self._ancho}, Área: {self.area()}'

# Ejemplo de uso
cuadrado = Cuadrado(5)
print(cuadrado)  # Ahora usa __str__ correctamente

rectangulo = Rectangulo(4, 6)
print(rectangulo)  # Ahora usa __str__ correctamente
