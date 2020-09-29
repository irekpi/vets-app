from django.contrib import admin
from django.urls import path, include
from users import views

app_name = 'users'

urlpatterns = [
    path('add-pet/', views.AddPetView.as_view(), name='add_pet'),
    path('all-pets/', views.AllPetsView.as_view(), name='all_pets'),
]