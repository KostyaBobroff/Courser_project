from django.db import models
from house.models import *

class SettingManager(models.Manager):

    def set_new_settings(self, bed_temp, water_temp, light_bath, light_bed):

        sett = self.filter(pk=1)
        if sett:
            sett = sett[0]
            sett.bedroom_temperature = bed_temp
            sett.water_temperature = water_temp
            sett.light_in_bathroom = light_bath
            sett.light_in_bedroom = light_bed
        else:
            sett = self.create(bedroom_temperature=bed_temp,
                                           water_temperature=water_temp,
                                           light_in_bathroom=light_bath,
                                           light_in_bedroom=light_bed)
        sett.save()