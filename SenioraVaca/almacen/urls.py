from django.urls import path
from . import views

app_name ='Almacen'

urlpatterns = [
    path('',views.index, name='index'),
    ]
