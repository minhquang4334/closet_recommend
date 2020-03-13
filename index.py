from flask import Flask, request, jsonify
from helpers import *
from api import *
from flask_cors import CORS
app = Flask(__name__, static_url_path='/static')
cors = CORS(app)

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

@app.route('/weather-conditions')
def weather_conditions():
    return jsonify(get_weather_conditions())

@app.route('/insta')
def get_insta_list():
    return jsonify(get_insta())

# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    config = load_config()
