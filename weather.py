"""weather.py"""
from pprint import pprint
import requests

def main():
    """Function that grabs weather data"""
    degree_sign = u'\N{DEGREE SIGN}'
    payload = {
        'zip': '63304,us',
        'units': 'imperial',
        'APPID': '05db8a6a0fbf5f2b42654061645412f5'
        }
    # This is grabbing OpenWeatherMap API data
    api_data = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)
    weather_values = api_data.json() #Get API request placed into json format
    #Weather values filtered on current temp and set to whole number
    current_temp = int(weather_values['main']['temp'])
    city = weather_values['name'] #City name pulled from weather values

    print(city)
    print('{}{} F'.format(current_temp, degree_sign))

if __name__ == '__main__':
    main()
