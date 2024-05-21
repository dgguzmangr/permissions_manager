from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    TYPES = [
        ('Jurídica', 'Jurídica'),
        ('Natural', 'Natural'),
    ]

    user_id = models.AutoField(primary_key=True)
    type = models.CharField('Type', max_length=20, choices=TYPES, blank=False, null=False)
    company_name = models.CharField('Company name', max_length=100, blank=False, null=False)
    name = models.CharField('Name', max_length=100, blank=False, null=False)
    last_name = models.CharField('Last name', max_length=100, blank=False, null=False)
    document = models.CharField('Document', max_length=15, blank=False, null=False)
    nit = models.CharField('NIT', max_length=18, blank=False, null=False)
    email = models.EmailField('Email', max_length=100, blank=False, null=False)
    password = models.CharField('Password', max_length=128, blank=False, null=False)
    status = models.BooleanField('Status', default=False, blank=False, null=False)

    class Meta:
        app_label = 'authApp'

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
