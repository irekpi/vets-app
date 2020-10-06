from django.contrib import admin
from django.urls import path, include
from animals import views

app_name = 'animals'

urlpatterns = [
    path('add-pet/', views.AddPetView.as_view(), name='add_pet'),
    path('detail-pet/<int:pk>', views.DetailPetView.as_view(), name='detail_pet'),
    path('all-pets/', views.AllPetsView.as_view(), name='all_pets'),
]
