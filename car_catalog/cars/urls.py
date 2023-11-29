
from django.urls import path
from .views import car_list, add_car, buy_car

urlpatterns = [
    path('car_list/', car_list, name='car_list'),
    path('add_car/', add_car, name='add_car'),
    path('buy_car/<int:car_id>/', buy_car, name='buy_car'),
]
