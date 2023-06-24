from flask import Flask, render_template, request
import requests
import time

app = Flask(__name__)

def get_weather_data(city):
    url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid=779c271986d91ab4f86362ce5d62e73c"
    r = requests.get(url)
    data = r.json()
    return data


def get_temperature(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=779c271986d91ab4f86362ce5d62e73c&units=metric"
    r = requests.get(url)
    data = r.json()
    temperature = data["main"]["temp"]
    return temperature


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)
        if len(weather_data) > 0:
            lat = weather_data[0]['lat']
            lon = weather_data[0]['lon']
            temp = get_temperature(lat, lon)
            return render_template('index.html', city=city, temperature=temp)
        else:
            error_message = "Invalid city name. Please try again."
            return render_template('index.html', error=error_message)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
