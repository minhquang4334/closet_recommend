import requests
import json
from helpers import *
from datetime import date, datetime
from datetime import timedelta
from dateutil import parser

config = load_config()
today = date.today()
maximum_time = date.today() + timedelta(config['maximum_time_delta'])

def get_5days_3hours_forcast_data(city_code='HaNoi', country_code='vn', units='metric'):
    url = config["fivedays_3hours_forcast_api"]
    url += 'q={},{}&units={}&APPID={}&lang={}'.format(city_code, country_code, units, config["api_key"], config['lang'])
    print (url)
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    return parsed

def get_data_from_file(city_code='hanoi'):
    with open(config["data_file_path"], "r") as read_file:
        data = json.load(read_file)
    try:
        return data[city_code]
    except:
        return False
        
    pass

def remove_unused_attributes(data):
    re = []
    for el in data:
        tmp = {}
        tmp['dt_txt'] = el['dt_txt']
        tmp['temp_min'] = el['main']['temp_min']
        tmp['temp_max'] = el['main']['temp_max']
        tmp['feels_like'] = (el['main']['temp_min'] + el['main']['temp_max'])/ 2
        tmp['weather'] = el['weather'][0]['main']
        tmp['description'] = el['weather'][0]['description']
        tmp['icon'] = el['weather'][0]['icon']
        r = handle_data_with_temp_condition(float(el['main']['temp_min']), float(el['main']['temp_max']), config)
        tmp['recommend'] = r['recommend']
        tmp['time'] = add_time(config, el)
        condition = add_condition(config, tmp['weather'])
        tmp['type'] = condition['japanese']
        tmp['images'] = condition['images']
        re.append(tmp)
    return re

def handle_data_with_temp_condition(min_temp=26, max_temp=30, config=None):
    recommends = config["closet_recommend"]
    average_temp = (min_temp + max_temp) / 2
    for key, r in recommends.items():
        if average_temp >= r['min'] and average_temp < r['max']:
            return r
    pass

def handle_data_with_date_condition(data, start_date=today, end_date=maximum_time):
    filter_data = [v for v in data if get_date(v['dt_txt']) >= start_date and get_date(v['dt_txt']) <= end_date]
    return filter_data

def handle_data_with_time_condition(data): #get morning, afternoon, night forcast
    filter_data = [v for v in data if is_in_config_time(config, get_time(v['dt_txt']))]
    return filter_data

def add_recommend_msg(data):
    for el in data:
        r = handle_data_with_temp_condition(float(el['main']['temp_min']), float(el['main']['temp_max']), config)
        el['recommend'] = r['recommend']
    return data

def handle_data(data, start_date=today, end_date=maximum_time):
    filter_data = handle_data_with_date_condition(data['list'])
    filter_data = handle_data_with_time_condition(filter_data)
    filter_data = add_recommend_msg(filter_data)
    # group by date
    list_dates = {}
    start = start_date
    # values = set(map(lambda x:(x['dt_txt']), filter_data))
    # results = [[y for y in filter_data if (y['dt_txt'])==x] for x in values]
    results = remove_unused_attributes(filter_data)
    return results

if __name__ == '__main__':
    print ()
