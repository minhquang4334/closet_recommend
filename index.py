from flask import Flask, request, jsonify
from helpers import *
from api import *
app = Flask(__name__, static_url_path='/static')
today = date.today()
maximum_time = date.today() + timedelta(config['maximum_time_delta'])
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/recommend')
def recommend():
    data = request.args
    if 'start_date' in data:
        start = get_date(data['start_date'])
    else:
        start = today

    if 'end_date' in data:
        end = get_date(data['end_date'])
    else:
        end = maximum_time

    if 'city_code' in data:
        city_code = data['city_code']
    else:
        city_code = 'hanoi'

    re = get_weather_recommend(city_code, start, end)
    return jsonify(re)

@app.route('/list')
def list_cities():
    return jsonify(cities_info())

# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)
    config = load_config()