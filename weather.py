import requests
import pprint

#API key
API='cb771e45ac79a4e8e2205c0ce66ff633'

#Enter your city's name
your_city=input('Enter City : ')

#Fetching URL
w_url="http://api.openweathermap.org/data/2.5/weather?q="+your_city+"&appid="+API+"?"
my_weather=requests.get(w_url).json()

#Converting result into .json file
pprint(my_weather)