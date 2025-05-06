import flask
from models.usuarios import Usuario
from config import db

class bixoController:
    @staticmethod
    def numbroBixo():
        if 'usuario' in flask.session:
            logado = Usuario.query.get(flask.session['usuario'])
            return flask.render_template('aposta.html', logado=logado)
        return flask.redirect(flask.url_for('registrar'))
    
    @staticmethod
    def definir_saldo():
        if 'usuario' not in flask.session:
            return flask.jsonify({'erro': 'não autenticado'}), 403

        data = flask.request.get_json()
        novo_saldo = float(data.get('saldo', 0))


        usuario: Usuario = Usuario.query.get(flask.session['usuario'])
        usuario.aumentarDinheiro(novo_saldo)
        db.session.commit()

        return flask.jsonify({ 'novo_saldo': usuario.dinheiro })
    
    @staticmethod
    def get_saldo():
        if 'usuario' not in flask.session:
            return flask.jsonify({'erro': 'não autenticado'}), 403

        usuario = Usuario.query.get(flask.session['usuario'])
        return flask.jsonify({ 'saldo': usuario.dinheiro })
