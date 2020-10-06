from django.contrib import admin
from django.urls import path, include
from users import views

app_name = 'users'

urlpatterns = [
    path('add-doctor-list/', views.AddDoctorList.as_view(), name='add_doctor_list'),
    path('add-doctor-list/<int:pk>/', views.AddDoctor.as_view(), name='add_doctor'),
    path('patients-list/', views.PatientsListView.as_view(), name='patients_doctor'),
]