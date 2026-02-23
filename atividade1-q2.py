'''Peça três notas (números decimais) ao usuário. Calcule a
média aritmética simples utilizando a fórmula:
$$M = \frac{n_1 + n_2 + n_3}{3}$$
Exiba o resultado formatado com duas casas decimais.
'''
def media(n1,n2,n3):
    media = n1+n2+n3/3
    return media

while True:
    try:
        n1 = float(input('digite a primeira nota: '))
        n2 = float(input('digite a segunda nota: '))
        n3 = float(input('digite a terceira nota: '))
        print(f'{media(n1,n2,n3):.2f}')
        if media > 10:
            raise ValueError
        break
    except ValueError:
        print('nota invalida, digite outra')


