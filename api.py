from data import *
from datetime import date, datetime, timedelta
from flask import jsonify
from helpers import *

today = date.today()
maximum_time = date.today() + timedelta(config['maximum_time_delta'])
#api get info of city code
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

#api get info of weather forcast
if __name__ == '__main__':
    print get_weather_recommend(start_date=get_date('2020-02-13'), end_date=get_date('2020-02-14'))
