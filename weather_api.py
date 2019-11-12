from flask import Flask, render_template, request
import requests
import pprint


app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with links to Fortune and Weather."""
    return render_template('index.html')

@app.route('/weatherform')
def weather_form():
    """Displays weather form."""
    return render_template('weather_form.html')

@app.route('/weather_results', methods=['GET', 'POST'])
def weather_results():
    """Displays weather results."""
    users_city = request.args.get('city')
    pp = pprint.PrettyPrinter(indent=4)

    weather_url ="http://api.openweathermap.org/data/2.5/weather?q="+ users_city +"&appid=2608f679d4594364525f6c6cc2246c79"

    response = requests.get(weather_url, params=params)
    response_json = response.json()
    pp.pprint(response_json)
    main_data = response_json["main"]

    temp_in_kelvin = main_data["main"]["temp"]
    return render_template('weather_results.html', city=city, temp=temp)
       
app.run()