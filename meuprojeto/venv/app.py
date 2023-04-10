from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home.html")
def homepage():
    return render_template("home.html")

@app.route("/contatos.html")
def contatos():
    return render_template("contatos.html")

@app.route("/quem_somos.html")
def quem_somos():
    return render_template("quem_somos.html")

if __name__ == "__main__":
    app.run(debug=True)
