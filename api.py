from data import *
from datetime import date, datetime, timedelta
from flask import jsonify
from helpers import *
import json
today = date.today()
maximum_time = date.today() + timedelta(config['maximum_time_delta'])
#api get info of city code
def get_insta():
    data = {}
    with open('./instagrams.json') as f:
        data = json.load(f)
    return data

def cities_info(): 
    config = load_config()
    list_city = config['list_city']
    return list_city

def get_weather_recommend(city_code='hanoi', start_date=today, end_date=maximum_time):
    weather_data = get_data_from_file(city_code)
    if weather_data == None:
        msg = {
            'msg': 'Error in City Code',
            'code': 201
        }
        return (msg)
    weather_data = handle_data_with_date_condition(weather_data, start_date, end_date)
    return (weather_data)

def get_weather_conditions():
    config = load_config()
    list_conditions = config['weather_conditions']
    return list_conditions

#api get info of weather forcast
if __name__ == '__main__':
    print (get_insta())
