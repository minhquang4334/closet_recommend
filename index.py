from flask import Flask
from helpers import *
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return app.send_static_file('index.html')

# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)
    config = load_config()