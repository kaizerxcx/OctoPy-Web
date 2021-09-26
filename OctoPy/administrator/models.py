from django.db import models
from user.models import User
# Create your models here.

class Administrator(User):
	admin_id = models.AutoField(primary_key=True)
	date_accepted = models.DateField(auto_now=True)
	class Meta:
		db_table="Administrator"