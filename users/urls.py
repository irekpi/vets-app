from django.contrib import admin
from django.urls import path, include
from users import views

app_name = 'users'

urlpatterns = [
    path('add-pet/', views.AddPetView.as_view(), name='add_pet'),
    path('detail-pet/<int:pk>', views.DetailPetView.as_view(), name='detail_pet'),
    path('all-pets/', views.AllPetsView.as_view(), name='all_pets'),
    path('add-doctor-list/', views.AddDoctorList.as_view(), name='add_doctor_list'),
    path('add-doctor-list/<int:pk>/', views.AddDoctor.as_view(), name='add_doctor'),
    path('patients-list/', views.PatientsListView.as_view(), name='patients_doctor'),
]