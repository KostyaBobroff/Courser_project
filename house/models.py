from django.contrib.auth.models import AbstractUser
from django.db import models
from house.managers import SettingManager

class User(AbstractUser):
    api_key = models.TextField(max_length=255)


class HouseSetting(models.Model):
    bedroom_temperature = models.IntegerField(default=21)
    water_temperature = models.IntegerField(default=80)
    light_in_bathroom = models.BooleanField(default=True)
    light_in_bedroom = models.BooleanField(default=True)
    objects = SettingManager()



    