import requests
import json
from helpers import *
from datetime import date, datetime
from datetime import timedelta
from dateutil import parser

config = load_config()
today = date.today()
maximum_time = date.today() + timedelta(config['maximum_time_delta'])


def get_sixteen_daily_data(city_code='HaNoi', country_code='vn', units='metric', cnt='16'):
    url = config["sixteendays_daily_forcast_api"]
    url += 'q={},{}&cnt={}&units={}&APPID={}&lang={}'.format(city_code, country_code, cnt, units, config["api_key_16days"], config['lang'])
    print (url)
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    return parsed


def handle_data_with_temp_condition(min_temp=26, max_temp=30, config=None):
    recommends = config["closet_recommend"]
    average_temp = (min_temp + max_temp) / 2
    for key, r in recommends.items():
        if average_temp >= r['min'] and average_temp < r['max']:
            return r
    pass

def remove_unused_attributes(data):
    re = []
    for el in data:
        tmp = {}
        tmp['dt_txt'] = datetime.utcfromtimestamp(el['dt']).strftime('%Y-%m-%d')
        tmp['temp_min'] = el['temp']['min']
        tmp['temp_max'] = el['temp']['max']
        tmp['temp_morn'] = el['feels_like']['morn']
        tmp['temp_day'] = el['feels_like']['day']
        tmp['temp_night'] = el['feels_like']['night']
        tmp['feels_like'] = el['feels_like']
        tmp['weather'] = el['weather'][0]['main']
        tmp['description'] = el['weather'][0]['description']
        tmp['icon'] = el['weather'][0]['icon']
        tmp['recommend'] = el['recommend']
        tmp['keywords'] = el['keywords']
        condition = add_condition(config, tmp['weather'])
        tmp['type'] = condition['japanese']
        tmp['images'] = condition['images']
        re.append(tmp)
    return re

def add_recommend_msg(data):
    for el in data:
        el['recommend'] = []
        el['keywords'] = []
        r_mor = handle_data_with_temp_condition(float(el['temp']['morn']), float(el['temp']['morn']), config)
        el['recommend'].append(r_mor['recommend'])
        el['keywords'].append(r_mor['keywords'])
        r_day = handle_data_with_temp_condition(float(el['temp']['day']), float(el['temp']['day']), config)
        el['recommend'].append(r_day['recommend'])
        el['keywords'].append(r_day['keywords'])
        r_night = handle_data_with_temp_condition(float(el['temp']['night']), float(el['temp']['night']), config)
        el['recommend'].append(r_night['recommend'])
        el['keywords'].append(r_night['keywords'])
    return data

if __name__ == '__main__':
    data = get_sixteen_daily_data()
    data = add_recommend_msg(data['list'])
    data = remove_unused_attributes(data)
    print (data)