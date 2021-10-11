from django.db import models
from user.models import User, Child
# Create your models here.

class Administrator(models.Model):
	admin_id = models.AutoField(primary_key=True)
	child_id =  models.ForeignKey(Child, null = False, blank = False, on_delete = models.CASCADE, related_name = "admin_user")
	date_accepted = models.DateField(auto_now=True)
	class Meta:
		db_table="Administrator"