from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateField('date created')


class Analysis(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    