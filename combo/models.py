from django.db import models

# city	city_ascii	lat	lng	country	iso2	iso3	admin_name	capital	population	id

class City(models.Model):
	city=models.CharField(max_length=22)
	city_ascii=models.CharField(max_length=22, null=True)
	latitude=models.CharField(max_length=22, null=True)
	longitude=models.CharField(max_length=22, null=True)
	country=models.CharField(max_length=22, null=True)
	iso2=models.CharField(max_length=22, null=True)
	iso3=models.CharField(max_length=22, null=True)
	admin=models.CharField(max_length=22, null=True)
	capital=models.CharField(max_length=22, null=True)
	population=models.CharField(max_length=22, null=True)
	id=models.CharField(max_length=22, primary_key=True)


class Language(models.Model):
	short= models.CharField(max_length=5)




# Create your models here.
