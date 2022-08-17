
from django.contrib import admin
from django.urls import path
from pybo import views
from django.conf.urls import include
from pybo import views
from django.urls import path
from facility import views

app_name = "facility"

urlpatterns = [
    path('map/', views.map, name='map'),
    path('download/', views.downloadFacilities, name='download'),
    path('facilitylist/', views.showFacilities, name='facilitylist'),
    path('facilitylist/getlocation/', views.getlocation, name='location_input')
]
