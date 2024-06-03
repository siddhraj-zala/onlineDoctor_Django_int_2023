from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    contact = models.CharField(max_length=10, null = True)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = "user"