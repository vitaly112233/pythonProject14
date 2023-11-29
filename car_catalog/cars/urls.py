#
# from django.urls import path
# from .views import car_list, add_car, buy_car, car_options
#
# urlpatterns = [
#     path('car_list/', car_list, name='car_list'),
#     path('add_car/', add_car, name='add_car'),
#     path('buy_car/<int:car_id>/', buy_car, name='buy_car'),
#     path('car_options/', car_options, name='car_options'),
# ]




from django.urls import path
from .views import car_list, car_catalog, buy_car, car_options, add_car

urlpatterns = [
    path('car_list/', car_list, name='car_list'),
    path('car_catalog/', car_catalog, name='car_catalog'),
    path('buy_car/<int:car_id>/', buy_car, name='buy_car'),
    path('car_options/', car_options, name='car_options'),
    path('add_car/', add_car, name='add_car'),
]
