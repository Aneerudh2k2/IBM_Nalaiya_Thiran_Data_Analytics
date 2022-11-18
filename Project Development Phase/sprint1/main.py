import sqlite3
from flask import Flask, request, Response
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__, static_url_path='')
bcrypt = Bcrypt(app)
CORS(app)


@app.get("/")
def homepage():
    return app.send_static_file("index.html")


@app.route('/register', methods=['POST'])
def register():
    conn = sqlite3.connect('database.db')
    form_data = request.get_json()
    email = form_data['email']
    password = form_data['password']
    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    if len(conn.execute(f'select * from users where email = "{email}"').fetchall()) != 0:
        conn.close()
        return Response(status=401)
    conn.execute(f'insert into users values("{email}","{pw_hash}")')
    conn.commit()
    return Response(status=200)


@app.route("/login", methods=['POST'])
def login():
    conn = sqlite3.connect('database.db')
    form_data = request.get_json()
    email = form_data['email']
    password = form_data['password']
    result = conn.execute(
        f'select * from users where email = "{email}"').fetchall()
    if len(result) == 0:
        conn.close()
        return Response(status=401)
    if bcrypt.check_password_hash(result[0][1], password):
        conn.close()
        return Response(status=200)
    conn.close()
    return Response(status=401)
