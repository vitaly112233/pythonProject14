


from django.urls import path
from .views import *
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('car_list/', car_list, name='car_list'),
    path('car_catalog/', car_catalog, name='car_catalog'),
    path('buy_car/<int:car_id>/', buy_car, name='buy_car'),
    path('car_options/', car_options, name='car_options'),
    path('add_car/', add_car, name='add_car'),
    # path('serializer/',serializer,name='serializer'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
