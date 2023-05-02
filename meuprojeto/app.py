from flask import Flask, render_template
#from flask_mysqldb 
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/quem_somos")
def quem_somos():
    return render_template("quem_somos.html")

if __name__ == "__main__":
    app.run(debug=True)

#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = '1234'
#app.config['MYSQL_DB'] = desafio03

#mysql = MySQL(app)