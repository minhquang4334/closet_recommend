import yaml
from datetime import date, datetime
from datetime import timedelta
from dateutil import parser

def load_config(path='./config.yaml'):
  with open(path) as fp:
    config = yaml.load(fp)
  return config

def get_date(str_datetime):
    return datetime.date(parser.parse(str_datetime))

def get_time(str_datetime):
    return datetime.time(parser.parse(str_datetime))

def is_in_config_time(config, time):
    temp_time = config['get_temp_time']
    str_time = "{}".format(time)
    for k, t in temp_time.items():
        if str_time == t: #compare string
            return True
    return False

def add_time(config, el):
    temp_time = config['get_temp_time']
    str_time = "{}".format(get_time(el['dt_txt']))
    for key, t in temp_time.items():
        if t == str_time:
            return key
    return "No data"
    pass
