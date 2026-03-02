from flask import Flask, request

def cadastrar():
    return
    
def entrar():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')
    return f'usuario: {usuario}, senha: {senha}'

def adicionarRotas(app: Flask):
    app.add_url_rule(rule='usuario/cadastrar', endpoint='cadastrar', view_func=cadastrar, methods= ['GET'])
    app.add_url_rule(rule='usuario/entrar', endpoint='entrar', view_func= entrar, methods= ['GET'])
    
    