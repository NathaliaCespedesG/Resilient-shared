# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('healthcare_professional', 'Healthcare Professional'),
        ('participant', 'Participant'),
    )
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='participant')