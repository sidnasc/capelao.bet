import flask
from models.usuarios import Usuario
from models.eventos import Eventos
from models.aposta import Aposta
from config import db

class UserController:

    @staticmethod
    def index():
        if 'usuario' in flask.session:
            logado = Usuario.query.get(flask.session['usuario'])
            return flask.render_template('user.html', logado=logado)
        
        return flask.redirect(flask.url_for('registrar'))
    
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
                if usuario.id == 1:
                    usuario.admin = True
                    db.session.commit()
                    print("admin virou admin")

                flask.session['usuario'] = usuario.id  
                print ("usuario logado: ", usuario.nome)
                return flask.redirect(flask.url_for('index'))

            else:
                print("nenhum usuario encontrado.")
                

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

        return flask.redirect(flask.url_for('login'))
    
    @staticmethod
    def logOut():
        flask.session.clear()
        return flask.redirect(flask.url_for('index'))
    
    
    
    
