from flask import Flask
app = Flask(__name__)

#ruta normal
@app.route('/')
def index():
    return '<h1>Hola mundooooo!</h1>'

#ruta dinamica
@app.route('/user/<name>')
def user(name):
    return '<h1>Holaa, %s!</h1>' % name
if __name__ == '__main__':
    app.run(debug=True)
