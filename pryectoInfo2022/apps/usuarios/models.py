from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    pass
    # nacionalidad = models.CharField(max_length = 30, null = True)
