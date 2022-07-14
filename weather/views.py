from django.shortcuts import render , redirect
import requests
from datetime import datetime
from django.http import Http404
from django.contrib import messages

def home(request):

    return render(request , 'home_page.html')


def search(request):
    query = request.POST.get('q')
    print(query)
    if query is not None:
        url = f'http://api.openweathermap.org/data/2.5/weather?q=london&appid=87d6864745382791a6bf6178daa3058d&units=metric'
        
    # url = 'http://api.openweathermap.org/data/2.5/forecast?q=tehran&appid=87d6864745382791a6bf6178daa3058d' 
    url = f'http://api.openweathermap.org/data/2.5/weather?q={query}&appid=87d6864745382791a6bf6178daa3058d&units=metric'

    r = requests.get(url=url).json()
    if r['cod'] == '404' or r['cod'] == '400':
        messages.error(request , "نام شهر وارد شده معتبر نیست")
        return redirect("/")
    print(r)

    today = r['main']['temp']
    weather = []
    date = datetime.now()

    if r:
        city_weather = {
            'today' : today,
            'main' : r['weather'][0]['main'],
            'location' : r['sys'],
            'city' : r['name'],
            'day' : date.day,
            'month' : date.month,
            'year' : date.year,
            'week' : date.weekday()
        }

        weather.append(city_weather)
        print(weather)
        

    return render(request , 'home_page.html' , {
        'weather' : weather[0],
    })
