from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name='Ivan'):
    edad=18
    my_list=[1,2,3,4,5,6,7,8,9]
    return render_template('user.html', name=name, age=edad, list=my_list)

if __name__ == "__main__":
    app.run(debug = True, port=5000)

