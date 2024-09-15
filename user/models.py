from django.db import models
from myadmin.models import *
from django.contrib.auth.models import User

class Register(models.Model):
	address = models.TextField()
	contact  = models.BigIntegerField()
	dob = models.DateField()
	gender = models.CharField(max_length=50)
	state = models.ForeignKey(State,on_delete=models.CASCADE)
	city = models.ForeignKey(City,on_delete=models.CASCADE)
	area = models.ForeignKey(Area,on_delete=models.CASCADE)
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	status = models.CharField(max_length=255,default='Pending')

	class Meta():
		db_table = 'register'

class Contact(models.Model):
	name 	= models.CharField(max_length=150)
	email 	= models.CharField(max_length=150)
	contact = models.BigIntegerField()
	message = models.TextField()
	date = models.DateField()
	

	class Meta():
		db_table = 'contact'


