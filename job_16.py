from data_16 import *
from schedule import * 
import schedule
import time
import json

def job(config):
    list_city = config['list_city']
    list_data_by_dates = {}
    for k, el in list_city.items():
        city_code = el['city_code']
        country_code = el['country_code']
        data = get_sixteen_daily_data(city_code=city_code, country_code=country_code)
        data = add_recommend_msg(data['list'])
        data = remove_unused_attributes(data)
        list_data_by_dates[city_code] = data
    js = json.dumps(list_data_by_dates)
    f = open(config["data_file_path"],"w+")
    f.write(js)
    f.close()

if __name__ == '__main__':
    config = load_config()
    # schedule.every().day.at("02:00").do(job)
    # while 1:
    #     schedule.run_pending()
    #     time.sleep(1)
    job(config)