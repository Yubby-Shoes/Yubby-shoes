from django.db import models

from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=255)
    default_size = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name + '-' + self.phone_number
