import requests
import json
from pprint import pprint

degree_sign = u'\N{DEGREE SIGN}'


#headers = {'APPID': '05db8a6a0fbf5f2b42654061645412f5'}

# This is grabbing OWM API data
api_data = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=63304,us&units=imperial&APPID=05db8a6a0fbf5f2b42654061645412f5')
weather_values = api_data.json() #Get API request placed into json format
current_temp = int(weather_values['main']['temp']) #Weather values filtered on current temp and set to whole number
city = weather_values['name'] #City name pulled from weather values

print(city)
print(current_temp, degree_sign, 'F')

