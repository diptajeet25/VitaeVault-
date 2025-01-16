from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE,  primary_key=True)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    dob = models.CharField(max_length=100)
    adress = models.TextField()
    clgname = models.CharField(max_length=100)
    clgdeg = models.CharField(max_length=100,default="Not Specified")
    clgyear = models.IntegerField()
    clgyear = models.CharField(max_length=100)
    clgdept = models.CharField(max_length=100,default="Not Specified")
    cls12name = models.CharField(max_length=100)
    cls12year = models.IntegerField()
    cls12group = models.CharField(max_length=100,default="Not Specified")
    cls10name = models.CharField(max_length=100)
    cls10year = models.IntegerField()
    cls10group = models.CharField(max_length=100,default="Not Specified")
    intrest = models.CharField(max_length=100)
    planguages = models.CharField(max_length=100)
    toolsandtech = models.CharField(max_length=100)
    projectname = models.CharField(max_length=100)
    projectdesc = models.TextField()
    project2name = models.CharField(max_length=100,default="Not Specified")
    project2desc = models.TextField(default="No project to describe")
    hobby1 = models.CharField(max_length=100)
    hobby2 = models.CharField(max_length=100)
    hobby3 = models.CharField(max_length=100)
    hobby4 = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname