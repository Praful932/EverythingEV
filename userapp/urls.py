from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('register/',views.register, name ='register'),
    # path('registerCustomer/',views.registerCustomer, name = 'registerCustomer'),
    path('stations_user/',views.stations_user,name = 'stations_user')
]

