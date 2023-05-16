from flask import Flask, render_template, request, url_for, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# conexão com o banco de dados
app.config['MYSQL_Host'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'contatos'

mysql = MySQL(app)

@app.route("/")
@app.route("/base")
def homepage():
    return render_template("home.html")

@app.route("/quem_somos")
def quem_somos():
    return render_template("quem_somos.html")

@app.route('/contatos', methods=['POST', 'GET'])
def contatos():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        
        cur = mysql.connection.cursor()
        cur.execute ("Insert INTO contatos (email, assunto, descricao) VALUES ('{email}', '{assunto}', '{descricao}')")
       
        mysql.connection.commit()
        
        cur.close()

        return 'sucesso'
    return render_template('contatos.html')


# rota usuários para listar todos os usuário no banco de dados.
@app.route('/user')
def user():
    cur = mysql.connection.cursor()

    user = cur.execute("SELECT * FROM contatos")

    if user > 0:
        userDetails = cur.fetchall()

        return render_template("user.html", userDetails=userDetails)

if __name__ == "__main__":
    app.run(debug=True)
