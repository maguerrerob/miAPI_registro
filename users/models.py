from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    correo_electronico = models.EmailField(unique=True)
    pais = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username



