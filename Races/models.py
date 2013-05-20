from django.db import models

# Create your models here.
class race(models.Model):
	race_name = models.CharField(max_length=50)
	def __unicode__(self):
		return self.race_name

class race_desc(models.Model):
	r_id = models.ForeignKey(race)
	race_desc = models.TextField()
	race_srd = models.TextField()
	race_stats = models.TextField()
	race_skills = models.TextField()
	race_misc = models.TextField()