import requests
from django.shortcuts import render
from .models import City_list
from .forms import City_list_form
from django.http import HttpResponseRedirect


# Create your views here.


def index(request):
    # by defaut of open weather map temperature is in kelvin.we can also convert it into celsius,degree etc.here
    # i'm using'&units=imperial' to get temperature in fahrenheit
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=188b48698b18f1dab768ab7226b12c91'

    '''
    # it will provide the city's weather
    city = 'Las Vegas'
    '''
    if request.method == "POST":

        form = City_list_form(request.POST)
        form.save()

        # this is used to avoid double submission of form
        return HttpResponseRedirect('/')

    form = City_list_form()
    # all the data of db will store in cities
    cities = City_list.objects.all()

    # it's a list
    weather_data = []
    for city in cities:

        # json is used for dictionary
        store = requests.get(url.format(city)).json()

        # (print(store.text) )  to print in console

        city_details = {
            # here city is used in internal py code and city_name is used for display name to the user. this city_name is the variable of model class City_list
            'city': city.city_name,
            # temp is used for temperature
            'temperature': store['main']['temp'],
            'description': store['weather'][0]['description'],
            'icon': store['weather'][0]['icon'],
        }

        # now the weather_data list will append or add all the data of city_details
        weather_data.append(city_details)

    context = {
        'weather_data': weather_data,  # now we are passing exact weather data
        'form': form,
    }
    return render(request, 'weather_app/index.html', context)
