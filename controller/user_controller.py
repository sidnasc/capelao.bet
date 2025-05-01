import flask
from models.usuarios import Usuario
from models.eventos import Eventos
from models.aposta import Aposta
from config import db
import datetime

class UserController:

    @staticmethod
    def index():
        if 'usuario' in flask.session:
            usuarios = Usuario.query.all()
            eventos = Eventos.query.all()
            apostas = Aposta.query.all()
            logado = Usuario.query.get(flask.session['usuario'])
            return flask.render_template('placeholder.html', usuarios=usuarios, eventos=eventos, apostas=apostas, logado=logado)
        return flask.redirect(flask.url_for('login'))
    
    @staticmethod
    def login():
        return flask.render_template('login.html')
    
    @staticmethod
    def registrar():
        return flask.render_template('registrar.html')
    
    @staticmethod
    def verificarLogin():
        if flask.request.method == 'POST':
            email = flask.request.form['email']
            senha = flask.request.form['senha']

            usuario: Usuario = Usuario.query.filter_by(email=email, senha=senha).first()

            if usuario:
                print(usuario.nome)
                flask.session['usuario'] = usuario.id  
                return flask.redirect(flask.url_for('index'))

            else:
                print("nenhum usuario achado")
                

        return flask.redirect(flask.url_for('login'))


    
    @staticmethod
    def add_usuarios():
        if flask.request.method == 'POST':
            nome =flask.request.form['nome']
            email = flask.request.form['email']
            senha = flask.request.form['senha']

            newUsuario = Usuario(nome=nome, email=email, senha=senha)
            db.session.add(newUsuario)
            db.session.commit()

        return flask.redirect(flask.url_for('index'))
    
    @staticmethod
    def add_evento():
        if flask.request.method == 'POST':
            nome =flask. request.form['nome']
            data_str = flask.request.form['data']

            data = datetime.datetime.strptime(data_str, '%Y-%m-%d').date()

            newEvento = Eventos(nome=nome, data=data)
            db.session.add(newEvento)
            db.session.commit()

        return flask.redirect(flask.url_for('index'))
    
    @staticmethod
    def add_aposta():
        if flask.request.method == 'POST':
            nome =flask. request.form['nome']
            data_str = flask.request.form['data']
            odd = flask.request.form['odd']
            idUser = flask.request.form['idUsuario']

            data = datetime.datetime.strptime(data_str, '%Y-%m-%d').date()

            newAposta = Aposta(nome=nome, data=data, odd=odd, idUsuario=idUser)
            db.session.add(newAposta)

            db.session.commit()

        return flask.redirect(flask.url_for('index'))
