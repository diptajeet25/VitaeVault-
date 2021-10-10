from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=150)
    desc = models.TextField()

    def __str__(self):
        return self.title