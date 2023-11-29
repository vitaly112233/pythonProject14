
from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from .forms import CarForm



def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()

    return render(request, 'add_car.html', {'form': form})


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})


def car_catalog(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})


def buy_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'buy_car.html', {'car': car})