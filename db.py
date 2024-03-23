from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Essas linhas importam as bibliotecas necessárias para criar um aplicativo 
# Flask e usar o SQLAlchemy para interagir com o banco de dados.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
# Essas linhas criam uma instância do aplicativo Flask e 
# configuram o SQLAlchemy para usar um banco de dados SQLite chamado site.db.
with app.app_context():
    # Seu código de acesso ao banco de dados aqui
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(20), unique=True, nullable=False)
        password = db.Column(db.String(60), nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
        posts = db.relationship('Post', backref='author', lazy=True)

        def __repr__(self):
            return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    # Esta classe define o modelo User para o banco de dados. 
    # Ele contém atributos como id, username, password, email e image_file.   
    class Post(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), nullable=False)
        date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
        content = db.Column(db.Text, nullable=False)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

        def __repr__(self):
            return f"Post('{self.title}', '{self.date_posted}')"

    new_user = User(username='admin', password='secret')
    db.session.add(new_user)
    db.session.commit()

    user = User.query.filter_by(username='admin').first()
    if user and user.password == 'secret':
        # Credenciais válidas
        pass
    else:
        # Credenciais inválidas
        pass