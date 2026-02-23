'''Peça dois valores (A e B). O programa 
deve inverter os valores (o que estava 
em A vai para B e vice-versa) e exibir 
os novos valores no terminal.'''
def inverter(a,b):
    C = a
    A = b
    B = C
    ab = [A,B]
    return ab

while True:
    try:
        a = input('digite o valor de A')
        b = input('digite o valor de B')
        inverter(a,b)
        print(f'A: ')
    except:
        print('')


    