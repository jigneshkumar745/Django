from django.urls import path
from . import views

urlpatterns = [
    path('Contact/', views.Contact,name='Cont'),
    path('Internship/', views.Internships,name='Intern'),
]
