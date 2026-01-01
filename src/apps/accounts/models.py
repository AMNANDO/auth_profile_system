from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    bio=models.TextField(blank=True)
    email=models.EmailField(unique=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name