from django.db import models

class Users1(models.Model):
	id = models.IntegerField(primary_key=True)
	age = models.IntegerField(max_length=10)
	class Meta:
		db_table = 'arc'
		app_label = "myproject" 