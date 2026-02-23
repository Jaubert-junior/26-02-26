'''Solicite o raio de um círculo e calcule
sua área. Utilize o valor aproximado 
de π = 3.14159. A fórmula é:
A = π ⋅ r
'''
from math import pi

def area(raio):
    A = pi * raio
    return A

while True:
    try:
        raio = float(input('digite o raio de um círculo: '))
        print(f'Área: {area(raio):.2f}')
        break
    except:
        print('raio do circulo inválido, digite outro')