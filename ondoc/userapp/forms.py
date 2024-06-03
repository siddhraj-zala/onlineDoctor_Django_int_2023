from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction

class DoctorCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'contact', 'password1', 'password2']
    
    @transaction.atomic
    def save(self, commit = True):
        user = super().save(commit = False)
        user.is_doctor = True
        if(commit):
            user.save()
        
        return user

class PatientCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'contact', 'password1', 'password2']
    
    @transaction.atomic
    def save(self, commit = True):
        user = super().save(commit = False)
        user.is_patient = True
        if(commit):
            user.save()
        
        return user