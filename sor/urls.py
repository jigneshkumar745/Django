from django.urls import path
from sor import views

urlpatterns = [
    path('Abu/',views.Abu,name='bol'),
    path('Blo/', views.Blo,name='sol'),
    ]