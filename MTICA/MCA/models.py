from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    regno = models.CharField(max_length=20, unique=True)
    college = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    plain_password = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.user.username
