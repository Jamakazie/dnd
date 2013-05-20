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

	
class people(models.Model):
	isknown = models.BooleanField(default=False)
	ismet = models.BooleanField(default=False)
	description = models.TextField()
	race = models.CharField(max_length=50)
	name = models.CharField(max_length =50)
	title = models.CharField(max_length=50)
	skill_sheet = models.ForeignKey(character)

class people_dm(models.Model):
	p_id = models.ForeignKey(people)
	dm_desc = models.TextField()
