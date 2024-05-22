from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password, check_password
from .role import Role

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
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
    email = models.EmailField('Email', max_length=100, blank=False, null=False, unique=True)
    username = models.CharField('Username', max_length=100, blank=False, null=False, unique=True)
    password = models.CharField('Password', max_length=128, blank=False, null=False)
    status = models.BooleanField('Status', default=False, blank=False, null=False)
    role = models.ManyToManyField(Role, related_name='users')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        app_label = 'authApp'

    def save(self, *args, **kwargs):
        self.username = self.email
        super(User, self).save(*args, **kwargs)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.email
