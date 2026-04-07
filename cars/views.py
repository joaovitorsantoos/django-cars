from django.shortcuts import render
from django.http import HttpResponse
from cars.models import Car


def cars_view(request):
    cars = Car.objects.filter(factory_year = '2025')

    return render(request, 'cars.html', { 'cars': cars })
    
