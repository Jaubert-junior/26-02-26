'''Crie um programa que peça o nome e o 
sobrenome do aluno separadamente e imprima 
uma mensagem de boas-vindas: “Olá [Nome] [Sobrenome], 
seja bem-vindo ao curso de Python!”.
'''
def saudacao(nome,sobrenome):
    print(f'Olá {nome} {sobrenome}, seja bem-vindo ao curso de Python!')
while True:
    try:
        nome = str(input('Digite o seu nome: '))
        sobrenome = str(input('Digite o seu  sobrenome: '))
        saudacao(nome, sobrenome)
        break
    except TypeError:
        print('nome invalido digite outro')