from django.urls import path
from . import views

urlpatterns = [
    path('', views.salary_form, name='salary_form'),
    path('calculate/', views.calculate_salary, name='calculate_salary'),
    path('jumble/', views.jumble_word, name='jumble_word'),
]
