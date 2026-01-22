from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete ,post_save
from django.dispatch import receiver
from client.models import client

class service_provider(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
        ("Suspended", "Suspended"),
    ]

    name = models.CharField(max_length=100)  
    phone = models.CharField(max_length=20) 
    service_provider_image = models.ImageField(upload_to='service_providers/',default='default_image.jpg', null=True, blank=True)  
    short_intro = models.TextField(max_length=255, null=True, blank=True)  
    bio = models.TextField(null=True, blank=True) 
    experience_years = models.IntegerField(null=True, blank=True) 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Active") 

    def __str__(self):
        return self.name


def createProfile(sender, instance, created, ** kwargs):
    if created:
        user = instance
        if user.is_staff == True:
            profile = service_provider.objects.create(
                user=instance,
                name=instance.username
            )
        else:
            profile = client.objects.create(
                user=instance,
                username=instance.username
            )



def DeleteProfile(sender, instance, ** kwargs):
    user_obj = instance.user
    user_obj.delete()


def EditProfile(sender, instance, created, ** kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.username = profile.name
        user.save()    


post_save.connect(createProfile,sender=User)
post_save.connect(EditProfile,sender=service_provider)
post_delete.connect(DeleteProfile,sender=service_provider)

