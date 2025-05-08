class Color:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f'{self.__dict__.__str__()}'
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

if __name__ == '__main__':
    c1 = Color('Rojo')
    print(c1)
