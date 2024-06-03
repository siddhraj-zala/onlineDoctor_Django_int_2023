from django.contrib import admin
from django.urls import path,include
from .views import DoctorRegisterView, PatientRegisterView, UserLogin
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('doctor_register/', DoctorRegisterView.as_view(), name = "doctor_register"),
    path('patient_register/', PatientRegisterView.as_view(), name = "patient_register"),
    path('login/', UserLogin.as_view(), name = "login"),
    path('logout/', LogoutView.as_view(next_page = "login"), name = "logout"),
    path('doctor_dashboard/', views.DoctorDashboard,),
    path('patient_dashboard/', views.PatientDashboard),
]