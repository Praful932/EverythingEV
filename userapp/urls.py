from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('stations/',views.stations, name='stations'),
    path('vehicledata_c/',views.vehicledata_c, name='vehicledata_c'),
    path('vehicledata_p/',views.vehicledata_p, name='vehicledata_p'),

]
