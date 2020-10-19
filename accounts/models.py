from django.db import models

from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name
