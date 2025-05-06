import flask
import os
import config
from controller.user_controller import UserController
from controller.admin_controller import AdminController
from controller.bixo_controller import bixoController
from controller.apostas_controller import ApostasController



app = flask.Flask(__name__, 
                  template_folder=os.path.join('view', 'templates'), 
                  static_folder=os.path.join('view', 'static'))

app.secret_key = os.urandom(24)
app.config.from_object(config.Config)

config.db.init_app(app)

with app.app_context():
    config.db.create_all()


app.add_url_rule('/', "index", UserController.index)

app.add_url_rule('/admin', "admin", AdminController.admin)

app.add_url_rule('/login', "login", UserController.login)
app.add_url_rule('/verificarLogin', "verficarLogin", UserController.verificarLogin, methods=['POST'])
app.add_url_rule('/logOut', "logOut", UserController.logOut)

app.add_url_rule('/registrar', "registrar", UserController.registrar)
app.add_url_rule('/add_usuario', 'add_usuario',  UserController.add_usuarios, methods=['POST'])

app.add_url_rule('/add_evento', 'add_evento',  AdminController.add_evento, methods=['POST'])
app.add_url_rule('/add_aposta', 'add_aposta',  AdminController.add_aposta, methods=['POST'])

app.add_url_rule('/numbroDoBixo', "numbroDoBixo", bixoController.numbroBixo)
app.add_url_rule('/definir_saldo', 'definir_saldo', bixoController.definir_saldo, methods=['POST'])
app.add_url_rule('/get_saldo', 'get_saldo', bixoController.get_saldo)

app.add_url_rule('/get_eventos', 'get_eventos', ApostasController.get_eventos)
app.add_url_rule('/get_apostas', 'get_apostas', ApostasController.get_apostas)
app.add_url_rule('/del_aposta', 'del_aposta', ApostasController.del_aposta, methods=['POST'])

app.add_url_rule('/reg_aposta', 'reg_aposta', ApostasController.reg_aposta, methods=['POST'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)