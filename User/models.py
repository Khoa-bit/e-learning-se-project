from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, **other):
        """
        Creates and saves a User 
        """
        user = self.model(
            email=self.normalize_email(email),
            **other
        )
        user.set_password(user.pk)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **other):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            **other
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = MyUserManager()
    
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12, blank=True)
    objects = MyUserManager()
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
