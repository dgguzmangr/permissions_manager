from django.db import models
from django.contrib.gis.db import models

class Ubication(models.Model):
    ubication_id = models.AutoField(primary_key=True)
    country = models.CharField('Country', max_length=100, blank=False, null=False)
    department = models.CharField('Department', max_length=100, blank=False, null=False)
    city = models.CharField('City', max_length=100, blank=False, null=False)
    neighborthood = models.CharField('Neighborthood', max_length=100, blank=False, null=False)
    address = models.CharField('Address', max_length=200, blank=False, null=False)
    postal_code = models.CharField('Postal code', max_length=20, blank=False, null=False)
    location = models.PointField('Location', blank=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        app_label = 'authApp'