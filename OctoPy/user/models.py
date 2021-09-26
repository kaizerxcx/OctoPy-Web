from django import db
from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField(default=6)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    date_registered = models.DateField(auto_now=True)
    class Meta:
        db_table="User"

class Child(User):
    child_id = models.AutoField(primary_key=True)
    isAtLevel1 = models.BooleanField(default=True)
    isAtLevel2 = models.BooleanField(default=False)
    isAtLevel3 = models.BooleanField(default=False)
    isAtLevel4 = models.BooleanField(default=False)
    isAtLevel5 = models.BooleanField(default=False)
    lastLogin = models.DateField(auto_now=True)
    class Meta:
        db_table="Child"

class Points:
    point_id = models.AutoField(primary_key=True)
    child_id =  models.ForeignKey(Child, null = False, blank = False, on_delete = models.CASCADE, related_name = "user_points")
    dateAcquired = models.DateField(auto_now=True)
    crazeOnPhonicPoints = models.IntegerField(default=0)
    wordKitPoints = models.IntegerField(default=0)
    alphaHopperPoints = models.IntegerField(default=0)
    mazeCrazePoints = models.IntegerField(default=0)
    readingSpreePoints = models.IntegerField(default=0)
    class Meta:
        db_table = "Points"

