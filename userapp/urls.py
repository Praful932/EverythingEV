from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('register/',views.register, name ='register'),
<<<<<<< HEAD
    path('registerConsumer/',views.registerConsumer, name = 'registerConsumer'),
    path('registerProvider/',views.registerProvider, name = 'registerProvider'),
    path("loginf/", auth_views.LoginView.as_view(
        template_name='userapp/login.html'), name='login'),  
    path("UpdateProfile/", views.UpdateProfile, name='UpdateProfile'),
    path("logoutf/", views.logoutf, name='logout'),
    path('ChargingStation/',views.ChargingStation, name = 'ChargingStation')
] 

# path("password-reset/", auth_views.PasswordResetView.as_view(
#         template_name='userapp/password_reset.html'), name='password_reset'),
#     path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(
#         template_name='userapp/password_reset_done.html'), name='password_reset_done'),    
#     path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
#         template_name='userapp/password_reset_confirm.html'), name='password_reset_confirm'),  
=======
    # path('registerCustomer/',views.registerCustomer, name = 'registerCustomer'),
    path('stations_user/',views.stations_user,name = 'stations_user')
]
>>>>>>> 4b13ba29fd6347e9151d5ad60f1e20e3a4bc17c3

