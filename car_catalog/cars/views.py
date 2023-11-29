#
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Car
# from .forms import CarForm
#
#
#
# def add_car(request):
#     if request.method == 'POST':
#         form = CarForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('car_list')
#     else:
#         form = CarForm()
#
#     return render(request, 'add_car.html', {'form': form})
#
#
# def car_list(request):
#     cars = Car.objects.all()
#     return render(request, 'car_list.html', {'cars': cars})
#
#
# def car_catalog(request):
#     cars = Car.objects.all()
#     return render(request, 'car_list.html', {'cars': cars})
#
#
# def buy_car(request, car_id):
#     car = get_object_or_404(Car, id=car_id)
#     return render(request, 'buy_car.html', {'car': car})

# views.py

from django.shortcuts import render, get_object_or_404
from .models import Car, CarOption
from .forms import CarForm, CarPurchaseForm

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

    if request.method == 'POST':
        form = CarPurchaseForm(request.POST)
        if form.is_valid():
            selected_options = form.cleaned_data['options']



            all_options = CarOption.objects.all()
            return render(request, 'car_options.html', {'car': car, 'selected_options': selected_options, 'all_options': all_options})

    else:
        form = CarPurchaseForm()

    return render(request, 'buy_car.html', {'car': car, 'form': form})

def car_options(request):

    if request.method == 'POST':
        selected_options = request.POST.getlist('options')

        options_objects = CarOption.objects.filter(id__in=selected_options)
        return render(request, 'car_options.html', {'selected_options': options_objects})

    return render(request, 'car_options.html', {'selected_options': []})
