from django.shortcuts import render
from django.http import HttpResponse
from cars.models import Car


def cars_view(request):
    cars = Car.objects.all()
    search = request.GET.get('search')

    if search:
        cars = Car.objects.filter(model__icontains=search).order_by('model')

    return render(
        request,
        'cars.html',
        {'cars': cars}
    )
    
