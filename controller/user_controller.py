import flask
from models.usuarios import usuario
from models.eventos import eventos
from config import db
import datetime

class UserController:

    @staticmethod
    def index():
        usuarios = usuario.query.all()
        evento = eventos.query.all()
        return flask.render_template('placeholder.html', usuarios=usuarios, eventos=evento)
    
    @staticmethod
    def add_usuarios():
        if flask.request.method == 'POST':
            nome =flask. request.form['nome']

            newUsuario = usuario(nome=nome)
            db.session.add(newUsuario)
            db.session.commit()

        return flask.redirect(flask.url_for('index'))
    
    @staticmethod
    def add_evento():
        if flask.request.method == 'POST':
            nome =flask. request.form['nome']
            data_str = flask.request.form['data']

            data = datetime.datetime.strptime(data_str, '%Y-%m-%d').date()

            newEvento = eventos(nome=nome, data=data)
            db.session.add(newEvento)
            db.session.commit()

        return flask.redirect(flask.url_for('index'))
