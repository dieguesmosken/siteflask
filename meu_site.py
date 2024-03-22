
from flask import Flask, render_template

app = Flask(__name__)

#criar a 1ª pagina do site

#route -> teuzinytbr.com /usuarios

#função -> o que voce quer exibir naquela pagina

#template

@app.route("/")
def homepage():
    return render_template("v2/index.html")

@app.route("/projetos")
def projetos():
    return render_template("v2/projects.html")

@app.route("/projetos/<projeto>")
def projeto(projeto):
    return render_template("v2/projects.html", projeto=projeto)

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

@app.route("/<nome_usuario>")
def homenome(nome_usuario):
    return render_template("v2/index.html", nome_usuario=nome_usuario)

#colocar o site no ar

if __name__ == "__main__":
    app.run(debug=True)

    #servidor do heroku
