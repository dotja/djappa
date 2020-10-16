from django.db import models


class MyTable(models.Model):
	app_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=50)
