import flask
from models.usuarios import Usuario
from models.eventos import Eventos
from models.aposta import Aposta
from config import db
import datetime

class UserController:

    @staticmethod
    def index():
        usuarios = Usuario.query.all()
        eventos = Eventos.query.all()
        apostas = Aposta.query.all()
        return flask.render_template('placeholder.html', usuarios=usuarios, eventos=eventos, apostas=apostas)
    
    @staticmethod
    def add_usuarios():
        if flask.request.method == 'POST':
            nome =flask. request.form['nome']

            newUsuario = Usuario(nome=nome)
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
