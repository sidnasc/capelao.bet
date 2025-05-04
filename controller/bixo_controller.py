import flask
from models.usuarios import Usuario

class bixoController:
    @staticmethod
    def numbroBixo():
        if 'usuario' in flask.session:
            logado = Usuario.query.get(flask.session['usuario'])
            return flask.render_template('aposta.html', logado=logado)
        return flask.redirect(flask.url_for('registrar'))