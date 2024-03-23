# Autor: Teuzin
from flask import Flask, render_template, request, redirect, url_for, session
# from db import db, User

# Inicializar o banco de dados
# db.create_all()

app = Flask(__name__)
app.config.from_object('config')
# db.init_app(app)

# Criar um contexto de aplicativo
with app.app_context():
    # Suas rotas e lógica de aplicativo aqui

#criar a 1ª pagina do site

#route -> teuzinytbr.com /usuarios

#função -> o que voce quer exibir naquela pagina

#rotas

    @app.route("/")
    def homepage():
        return render_template("index.html")

    @app.route("/projetos")
    def projetos():
        return render_template("projects.html")

    @app.route("/projetos/<projeto>")
    def projeto(projeto):
        return render_template("projects.html", projeto=projeto)

    @app.route("/sobre")
    def sobre():
        return render_template("about.html")

    @app.route("/sobre/?usuario=<usuario>")
    def usuario(usuario):
        return render_template("about.html", usuario=usuario)

    # rotas de registro e login
    @app.route("/login")
    def login():
        return render_template("login.html")


    # @app.route('/register', methods=['POST'])
    # def register():
    #     username = request.form.get('username')
    #     password = request.form.get('password')

    #     user = User(username=username, password=password)
    #     db.session.add(user)
    #     db.session.commit()

    #     return redirect(url_for('login'))

    # @app.route('/login', methods=['POST'])
    # def login():
    #     username = request.form.get('username')
    #     password = request.form.get('password')

    #     user = User.query.filter_by(username=username).first()

    #     if user and user.password == password:
    #         session['logged_in'] = True
    #         return redirect(url_for('home'))

    #     return redirect(url_for('login'))


# Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)