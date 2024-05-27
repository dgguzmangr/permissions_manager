from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Phone(models.Model):
    phone_id = models.AutoField(primary_key=True)
    phone_number = PhoneNumberField()
    active = models.BooleanField(default=True)

    class Meta:
        app_label = 'authApp'