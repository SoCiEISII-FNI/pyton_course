from flask import Flask
from flask import request


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
@app.route('/hola/')
@app.route('/hola/<name>/')
@app.route('/hola/<name>/<int:num>')
def como(name = 'este es un paramentro por falla',num='nada'):
    return 'buenos dias: {} {}'.format(name,num)

if __name__ == "__main__":
    app.run(debug=True, port=5000)



https://www.youtube.com/watch?v=OFAdgCjnRtA&list=PLagErt3C7iltAydvN6SgCVKsOH4xQQKsk&index=9
