from django.db import models
from django.contrib.auth.models import User


class client(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ("male", "male"),
        ("female", "female"),
        ("Prefer not to say","Prefer not to say")
    ]
    username = models.CharField(max_length=50)  
    phone = models.CharField(max_length=20) 
    client_image = models.ImageField(upload_to='client/',default='default_image.jpg', null=True, blank=True,max_length=255)  
    gender = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Prefer not to say") 
    birth_date = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.username


