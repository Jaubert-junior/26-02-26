'''Desenvolva um script que receba 
um valor em metros e exiba o equivalente
em centímetros e milímetros no terminal.
'''
def paraCent(m):
    return m*100

while True:
    try:
        metros = float(input('digite uma quantia em metros: '))
        print(f'em centimetros: {paraCent(metros):.2f}')
        break
    except ValueError:
        print('quantia inválida, digite outra')