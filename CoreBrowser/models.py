from django.db import models
#from django.contrib.postgres.fields import ArrayField



# Create your models here.
class Well(models.Model):
	
	file_num = models.TextField(primary_key = True)
	api = models.BigIntegerField(blank=True, null=True)
	box_count = models.IntegerField(blank=True, null=True)
	operator = models.TextField(blank=True, null=True)
	lease = models.TextField(blank=True, null=True)
	well_num = models.TextField(blank=True, null=True)
	sec = models.IntegerField(blank=True, null=True)
	twn = models.IntegerField(blank=True, null=True)
	twn_d = models.TextField(blank=True, null=True)
	rng = models.IntegerField(blank=True, null=True)
	rng_d = models.TextField(blank=True, null=True)
	qq = models.TextField(blank=True, null=True)
	latitude = models.FloatField(blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)
	county = models.TextField(blank=True, null=True)
	state = models.TextField(blank=True, null=True)
	field = models.TextField(blank=True, null=True)

	class Meta():
		db_table = "wells"
		ordering = ["file_num"]

	def get_STR(self):
		return f"{self.sec} - {self.twn}{self.twn_d} - {self.rng}{self.rng_d}"

	def get_well_summary(self):
		s1 = f"{self.file_num} \t {self.api}\n"
		s2 = f"{self.operator} \t {self.well_num} \t {self.lease}\n"
		s3 = self.get_STR() + f"\t {self.county} Co. \t ({self.box_count} boxes)\n"
		return (s1 + s2 + s3)

	def __str__(self):
		return self.get_well_summary()


class Box(models.Model):
	file_num = models.ForeignKey(Well(), on_delete=models.CASCADE)
	box_num = models.IntegerField(blank=True, null=True)
	formation = models.TextField(blank=True, null=True)
	top = models.TextField(blank=True, null=True)
	bottom = models.TextField(blank=True, null=True)
	diameter = models.TextField(blank=True, null=True)
	box_type = models.TextField(blank=True, null=True)
	sample_type = models.TextField(blank=True, null=True)
	condition = models.TextField(blank=True, null=True)
	restrictions = models.TextField(blank=True, null=True)
	comments = models.TextField(blank=True, null=True)

	class Meta():
		db_table = "boxes"

	def __str__(self):
		s1 = f"file: {self.file_num} \t box: {self.box_num} \t {self.formation}\n"
		s2 = f"{self.top} - {self.bottom}\n"
		s3 = f"{self.comments}\n"

		return (s1 + s2 + s3)
