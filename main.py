from flask import Flask
from routes import usuarioRouter, postRouter, ola


app = Flask(__name__)

usuarioRouter.adicionarRotas(app=app)
postRouter.adicionarRotas(app=app)