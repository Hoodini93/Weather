"""weather.py"""
import requests
from prettytable import PrettyTable
def main():
    """Function that grabs weather data"""
    degree_sign = u'\N{DEGREE SIGN}'
    zipcode = ['63304,us', '90001,us', '10001,us']
    weather_chart = PrettyTable(['', 'Current', 'High', ' Low'])
    for each in zipcode:
        payload = {
            'zip': each,
            'units': 'imperial',
            'APPID': '05db8a6a0fbf5f2b42654061645412f5'
            }
        # This is grabbing OpenWeatherMap API data
        api_data = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)
        weather_values = api_data.json() #Get API request placed into json format
        #Weather values filtered on current temp and set to whole number
        high_temp = int(weather_values['main']['temp_max'])
        low_temp = int(weather_values['main']['temp_min'])
        current_temp = int(weather_values['main']['temp'])
        city = weather_values['name'] #City name pulled from weather values
        weather_chart.add_row([city, current_temp, high_temp, low_temp])
    print(weather_chart)

if __name__ == '__main__':
    main()
