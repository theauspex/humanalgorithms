from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Color(models.Model):
	color_name = models.CharField(max_length = 30, default="")
	image_url = models.CharField(max_length = 100, default="")