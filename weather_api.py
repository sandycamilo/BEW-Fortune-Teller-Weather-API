from flask import render_template, request
# import pprint # to print dictionaties/json objects in terminal 
import requests


def weather_form():
    """Displays weather form."""
    return render_template('weather_form.html')

def weather_results():
    """Displays weather results."""
    users_city = request.args.get('city')
    # pp = pprint.PrettyPrinter(indent=4)
   
    weather_url ="http://api.openweathermap.org/data/2.5/weather?q="+ users_city +"&appid=2608f679d4594364525f6c6cc2246c79"

    response = requests.get(weather_url)
    response_json = response.json()
    # pp.pprint(response_json)
    

    temp_in_kelvin = response_json["main"]["temp"]
    return render_template('weather_results.html', city=users_city, temp=temp_in_kelvin)
       
