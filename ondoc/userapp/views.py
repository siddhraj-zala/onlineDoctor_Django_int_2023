from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from .forms import DoctorCreationForm, PatientCreationForm
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
class DoctorRegisterView(CreateView):
    model = User
    form_class = DoctorCreationForm
    template_name = "userapp/doctor_register.html"
    success_url = "/userapp/login"

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        print(email)
        sendMail(email)
        return super().form_valid(form)


class PatientRegisterView(CreateView):
    model = User
    form_class = PatientCreationForm
    template_name = "userapp/patient_register.html"
    success_url = "/userapp/login"

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        print(email)
        sendMail(email)
        return super().form_valid(form)
    

def sendMail(to):
    subject = 'welcome to on-Doctor'
    message = 'Hi, this is welcome mail'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [to,]
    send_mail( subject, message, email_from, recipient_list )
    return True


class UserLogin(LoginView):
    template_name = "userapp/login.html"

    def get_success_url(self):  # also used--> def get_redirect_url(self): 
        print(self.request.user)
        if self.request.user.is_authenticated:
            print("user is authenticated")
            print("doctor--->", self.request.user.is_doctor)

            if self.request.user.is_superuser:
                return "/admin/"
            elif self.request.user.is_doctor:
                return "/userapp/doctor_dashboard/"
            elif self.request.user.is_patient:
                return "/userapp/patient_dashboard/"
        else:
            return "/userapp/login"  
  
                  
def DoctorDashboard(request):
    return render(request, "userapp/doctor_dashboard.html")


def PatientDashboard(request):
    return render(request, "userapp/patient_dashboard.html")


def Home(request):
    return render(request, "index.html")


