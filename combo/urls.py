from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
path('', views.home, name='home'),
path('tran/', views.tran, name='tran'),
path('detect/', views.detect, name='detect'),
path('translate/', views.translate, name='translate'),
path('code/', views.code, name='code'),
path('fromqr/', views.fromqr, name='fromqr'),
path('toqr/', views.toqr, name='toqr'),
path('weather/', views.weather, name='weather'),
path('getweather/', views.getweather, name='getweather'),
]