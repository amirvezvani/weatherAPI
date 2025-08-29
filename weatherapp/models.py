from django.db import models

# Create your models here.

class WeatherModel(models.Model):
    city=models.CharField(max_length=25)
    temperature=models.FloatField()
    humidity=models.FloatField()
    description=models.CharField(max_length=20)
    date=models.DateTimeField(auto_now_add=True)
    icon=models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.city}'