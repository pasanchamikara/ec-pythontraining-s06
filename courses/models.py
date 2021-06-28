from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    duration = models.IntegerField()

class Lecturer(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    course = models.ManyToManyField(Course)