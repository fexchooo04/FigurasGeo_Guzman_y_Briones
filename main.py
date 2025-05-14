from SRC.Circunferencia import Circunferencia
from SRC.Cuadrado import Cuadrado
from SRC.Rectangulo import Rectangulo

c1 = Cuadrado(lado=6, color= 'rojo')
c2 = Cuadrado(lado=7, color= 'amarillo')
c3 = Cuadrado(lado=8, color= 'blanco')
c4 = Cuadrado(lado=9, color= 'verde')
c5 = Cuadrado(lado=4, color= 'negro')
r1 = Rectangulo(alto=8, ancho=7 , color= 'negro')
r2 = Rectangulo(alto=2, ancho=6,  color= 'verde')
r3 = Rectangulo(alto=1, ancho=6, color= 'blanco')
r4 = Rectangulo(alto=4, ancho=5, color= 'rojo')
r5 = Rectangulo(alto=7, ancho=9, color= 'amarillo')
circ = Circunferencia(radio=9, color = 'coral')

def calcular_dimensiones(lista):
    for fg in lista:
        if isinstance(fg, Rectangulo):
            print('Rectangulo')
        elif isinstance(fg, Cuadrado):
            print('Cuadrado')
        print(fg)
        print(f'Area: {fg.area()}')
        print(f'Perimetro: {fg.perimetro()}')
        print('*'.center(50, '*'))


lista_fg = [c1, c2, c3, c4, c5, r1, r2, r3, r4, r5, circ]
calcular_dimensiones(lista_fg)