from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("weather_app.html")

@app.route("/weatherapp", methods = ['POST' , 'GET'])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"
    param = {'q': request.form.get("city"),
    'appid': "2d395903ac3a9d88a3c25c5d2326d70a",
    'units': "metric"}
    response = requests.get(url, params= param)
    data = response.json()
    return f"data :{data}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 5002)