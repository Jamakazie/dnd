from django.db import models

# Create your models here.
class character(models.Model):
	stats = models.TextField()
	skills = models.TextField()
	saves = models.TextField()
	attack_bonus = models.TextField()
	description = models.TextField()
	items = models.TextField()
	alignment = models.TextField()
	race = models.TextField()
	name = models.TextField()
	gold = models.TextField()
	level = models.TextField()
	cclass = models.TextField()
