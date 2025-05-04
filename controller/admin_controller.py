import flask
from models.usuarios import Usuario
from models.eventos import Eventos
from models.aposta import Aposta
from config import db
import datetime


class AdminController:

    @staticmethod
    def admin():
        if 'usuario' in flask.session:
            user: Usuario = Usuario.query.get(flask.session['usuario'])

            if user.admin:
                usuarios = Usuario.query.all()
                eventos = Eventos.query.all()
                apostas = Aposta.query.all()
                return flask.render_template('admin.html', usuarios=usuarios, eventos=eventos, apostas=apostas, logado=user)
            
        return flask.abort(403)

    @staticmethod
    def add_aposta():
        if flask.request.method == 'POST':
            # data_str = flask.request.form['data']
            odd = flask.request.form['odd']
            idEvento = flask.request.form['idEvento']

            # data = datetime.datetime.strptime(data_str, '%Y-%m-%d').date()

            newAposta = Aposta(odd=odd, idEvento=idEvento)
            db.session.add(newAposta)

            db.session.commit()

        return flask.redirect(flask.url_for('admin'))
    
    @staticmethod
    def add_evento():
        if flask.request.method == 'POST':
            data_str = flask.request.form['data']
            nome = flask.request.form['nome']
            oddCasa = flask.request.form['oddCasa']
            oddVisitante = flask.request.form['oddVisitante']

            data = datetime.datetime.strptime(data_str, '%Y-%m-%d').date()

            newEvento = Eventos(data=data, nome=nome, oddCasa=oddCasa, oddVisitante=oddVisitante)
            db.session.add(newEvento)
            db.session.commit()

        return flask.redirect(flask.url_for('admin'))