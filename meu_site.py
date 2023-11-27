from flask import Flask, render_template

app = Flask(__name__)

#criar a 1ª pagina do site

#route -> teuzinytbr.com /usuarios

#função -> o que voce quer exibir naquela pagina

#template

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

#colocar o site no ar

if __name__ == "__main__":
    app.run(debug=True)

    #servidor do heroku
