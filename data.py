import requests
import json
from helpers import *

url = "https://api.openweathermap.org/data/2.5/forecast?q=HaNoi,vn&units=metric&APPID=2c07c4b723a79973f52a9f847a271f34"
 
response = requests.get(url)
data = response.text
parsed = json.loads(data)
print (parsed["list"][0])

def get_5days_3hours_forcast_data(config, city_code='HaNoi', country_code='vn', units='metric'):
    url = config["fivedays_3hours_forcast_api"]
    url += 'q={},{}&%units={}&APPID={}'.format(city_code, country_code, units, config["api_key"])
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    return parsed
    
if __name__ == '__main__':
    config = load_config()
    print get_5days_3hours_forcast_data(config)
