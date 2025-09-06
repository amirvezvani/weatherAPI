from django.shortcuts import render
from django.views import View
import requests
from .models import WeatherModel
import datetime
from django.contrib import messages

# Create your views here.

class Index(View):
    def post(self,request):
        try:
            city=request.POST['city']
            url='https://api.openweathermap.org/data/2.5/weather'
            with open('apikey.txt','r') as f:
                appid=f.read().strip()
            units='metric'
            params={'q':city,
                'appid':appid,
                'units':units,
                }
            res=requests.get(url=url,params=params)
            if res.status_code==200:
                data=res.json()
                temperature=data['main']['temp']
                humidity=data['main']['humidity']
                description=data['weather'][0]['description']
                icon=data['weather'][0]['icon']
                date=datetime.datetime.now()
                WeatherModel.objects.create(
                    city=city,
                    temperature=temperature,
                    humidity=humidity,
                    description=description,
                    icon=icon
                )
            return render(request,'weatherapp/index.html',{'data':data,'date':date})  
        except UnboundLocalError:
            error='There is not any city with this name!'
            return render(request,'weatherapp/index.html',{'error':error}) 

    def get(self,request):
        return render(request,'weatherapp/index.html')