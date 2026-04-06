from django.shortcuts import render
from django.http import HttpResponse
from cars.models import Car


def cars_view(request):
    cars = Car.objects.all()

    return render(request, 'cars.html', { 'cars': cars })
    
