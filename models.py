from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.text import slugify

class UserManager(BaseUserManager):
    def create_user(self, email, name, surname, password):
        if not email:
            raise ValueError("The Email field must be set")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            surname=surname,
        )
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, name, surname, password):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            surname=surname,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    date_of_birth = models.DateField(blank=True,
                                     null=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    password = models.CharField(max_length=10)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_active
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Event(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    event_date = models.DateField()
    event_time = models.TimeField()
    age_range = models.PositiveIntegerField()
    volunteers_quantity_needed = models.PositiveIntegerField()
    event_place = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)


    def __str__(self):
        return f'{self.title} - {self.category} - {self.event_date} - {self.volunteers_quantity_needed}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(f'{self.title} - {self.category} - {self.description}')
        super().save(force_insert, force_update, using, update_fields)

