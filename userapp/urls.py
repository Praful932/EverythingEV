from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from userapp.views import (ChargingStationProviderDeleteView, MaintenanceMan, SearchListView)

# ChargingStation - CS
urlpatterns = [
    path('', views.index, name='index'),
    path('check/', views.check, name='check'),
    path('register/', views.register, name='register'),
    path('registerConsumer/', views.registerConsumer, name='registerConsumer'),
    path('registerConsumerSocial/', views.registerConsumerSocial, name='registerConsumerSocial'),
    path('registerProvider/', views.registerProvider, name='registerProvider'),
    path("UpdateProfile/", views.UpdateProfile, name='Profile'),
    path('Charging-Station/add/', views.AddChargingStation, name='AddChargingStation'),
    path('Provider-Dashboard/', views.ProviderDashboard, name='Provider-Dashboard'),
    path('Charging-Station/analytics/<int:pk>', views.ChargingStationAnalytics, name='Charging-Station-Analytics'),
    path('Charging-Station/dashboard/<int:pk>', views.ChargingStationDashboard, name='Charging-Station-Dashboard'),
    path('station/<int:pk>/delete/', ChargingStationProviderDeleteView.as_view(), name='DeleteStation'),
    path('Charging-Station/all-stations/', views.ChargingStationConsumer, name='Charging-Station-CLV'),
    path('charge-poolong-form/',views.Charpoolingform,name="chargepoolingform"),
    path('Charge-Pooling/', views.ChargePooling, name='Charge-Pooling'),
    path('Route-Your-Way/', views.RouteYourWay, name='Route-Your-Way'),
    path('registerMaintenance/', MaintenanceMan.as_view(), name="Register-As-Maintenance"),
    path('Maintenance-man/dashboard', views.MaintenanceDashboard, name='Maintenance-man-dashboard'),
    path('Maintenance-man/view-all', SearchListView.as_view(), name='All-Maintenance-Man'),
    path('Maintenance-man/complaints', views.MaintenanceComplaint, name='Complaint-Dashboard'),
    path('book/<int:pk>', views.bookMaintenanceMan, name="bookingMm"),
    path('ajax/supportrequest', views.SupportRequest, name="SupportRequest"),
    path('faqs/', views.faq, name="faqs"),
    path('why-choose-ev/', views.WhyChooseEV, name="Why-Choose-EV"),
    path('sales-page/', views.salesPage, name="sales-page"),
    path('sales-page/two-wheelers', views.twoWheelers, name="two-wheelers"),
    path('sales-page/three-wheelers', views.threeWheelers, name="three-wheelers"),
    path('sales-page/four-wheelers', views.fourWheelers, name="four-wheelers"),
    path('sales-page/heavy-vehicles', views.heavyVehicles, name="heavy-vehicles"),
    path('buildcs/', views.BuildCs, name="BuildCs"),
    path('savings-calculator/', views.savingsCalculator, name="savings-calculator"),
    path('dash-welcome/', views.dashwelcome, name="dash-welcome"),
    path('live_data/', views.live_data, name="Live-Data"),
    path('demo/',views.demo, name = "demo"),
    path('demo2/',views.demo2,name= "demo2"),
    path('demo3/',views.demo3,name= "demo2")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
