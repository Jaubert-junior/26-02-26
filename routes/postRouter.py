from flask import Flask, request

def criar():
    titulo = request.args.get('titulo')
    texto = request.args.get('texto')
    return f'titulo: {titulo} texto: {texto}'

def visualizar():
    return 'exibindo todos os posts do usuario'

def adicionarRotas(app: Flask):
    app.add_url_rule(rule='/post/criar', endpoint='criar', view_func=criar, methods=['GET'])
    app.add_url_rule(rule='/post/visualizar', endpoint='visualizar', view_func=visualizar, methods=['GET'])
    