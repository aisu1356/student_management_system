from django.contrib.auth.models import AbstractUser
from django.db import models

class Student(AbstractUser):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    course = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField('auth.Group', related_name='student_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='student_permissions', blank=True)

    def __str__(self):
        return self.name
