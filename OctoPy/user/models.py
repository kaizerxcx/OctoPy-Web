from django import db
from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField(default=6)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default="NA")
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
    class Meta:
        db_table="Child"

class Points(models.Model):
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

class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
#    child_id =  models.ForeignKey(Child, null = False, blank = False, on_delete = models.CASCADE, related_name = "user_feedback")
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254)
    subject = models.CharField(max_length=100)
    feedback = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True)
    isRead = models.BooleanField(default=False)
    class Meta:
        db_table = "Feedback"


class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    child_id =  models.ForeignKey(Child, null = False, blank = False, on_delete = models.CASCADE, related_name = "user_request")
    status = models.CharField(max_length=100, default="Pending")
    date = models.DateField(auto_now=True)
    content = models.CharField(max_length=100)
    isRead = models.BooleanField(default=False)
    class Meta:
        db_table = "Request"

class Notification(models.Model):
	notification_id = models.AutoField(primary_key=True)
	sender = models.ForeignKey(Child, null = False, blank = False, on_delete = models.CASCADE, related_name = "notification_sender")
	receiver = models.CharField(max_length=500)
	content = models.CharField(max_length=500)
	datetime = models.DateTimeField(auto_now=True)
	isRead = models.BooleanField(default=False)
	class Meta:
		db_table="Notification"

class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    child_id =  models.ForeignKey(Child, null = False, blank = False, on_delete = models.CASCADE, related_name = "user_login")
    datetime = models.DateTimeField(auto_now=True)
    lastLogin =  models.CharField(max_length=10)
    class Meta:
        db_table="Login"