import requests # type: ignore
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import WeatherSummary
import json
from datetime import datetime, timedelta
import pytz # type: ignore

API_KEY = '13e0194df2d25e230fc4e1ca7a91e5f5'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def fetch_weather_data():
    summaries = []
    for city in CITIES:
        complete_url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
        response = requests.get(complete_url)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            weather_condition = data['weather'][0]['main']
            summaries.append((city, temp, feels_like, weather_condition))
    return summaries

def index(request):
    weather_data = fetch_weather_data()
    return render(request, 'index.html', {'weather_data': weather_data})

def summary(request):
    weather_summaries = WeatherSummary.objects.all()
    alerts = []
    for summary in weather_summaries:
        if summary.max_temperature > 35:  # Example condition
            alerts.append(f"Alert! High temperature recorded on {summary.date}: {summary.max_temperature}°C")

    return render(request, 'summary.html', {'weather_summaries': weather_summaries, 'alerts': alerts})
