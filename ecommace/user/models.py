from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager

)
class UserManager(BaseUserManager):
    def create_user(self,email,password = None,is_active = True,is_staff = False,is_admin = False):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have an password")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password) # change user password
        user_obj.save()
        return user_obj

    def create_staff(self,email,password = None):
        user = self.create_user(
            email,
            password = password,
            is_staff= True
        )
        return user

    def create_superuser(self,email,password = None):
        user = self.create_user(
            email,
            password = password,
            is_staff= True,
            is_admin= True
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length =100 ,unique = True)
    full_name = models.CharField(max_length =100)
    last_name = models.CharField(max_length =100)
    active = models.BooleanField(default = True)
    staff = models.BooleanField(default = False)
    admin = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    def get_last_name(self):
        return self.last_name


    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

class Profile(models.Model):
   user   = models.OneToOneField(User,on_delete = models.CASCADE)
  #extend extra data

class GuestEmail(models.Model):
    email = models.EmailField(max_length =100,unique = True)
    active = models.BooleanField(default = True)
    update = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.email