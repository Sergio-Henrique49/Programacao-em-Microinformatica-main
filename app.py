from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/contatos")
def contatos():
    return render_template("contato.html")

@app.route("/quem_somos")
def quem_somos():
    return render_template("quem.html")

if __name__ == "__main__":
    app.run(debug=True)
