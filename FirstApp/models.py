from django.db import models
from UserApp.models import User

# Create your models here.


class Address(models.Model):
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.city


class ITJobs(models.Model):
    job_company = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30)
    job_description = models.TextField()
    job_designation = models.CharField(max_length=30)
    job_experience = models.FloatField()
    job_package = models.FloatField()
    job_position = models.IntegerField()
    job_date_from = models.DateField()
    job_date_to = models.DateField()
    job_location = models.ForeignKey(Address, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.job_company


class MECHJobs(models.Model):
    job_company = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30)
    job_description = models.TextField()
    job_designation = models.CharField(max_length=30)
    job_experience = models.FloatField()
    job_package = models.FloatField()
    job_position = models.IntegerField()
    job_date_from = models.DateField()
    job_date_to = models.DateField()
    job_location = models.ForeignKey(Address, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.job_company


class CIVILJobs(models.Model):
    job_company = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30)
    job_description = models.TextField()
    job_designation = models.CharField(max_length=30)
    job_experience = models.FloatField()
    job_package = models.FloatField()
    job_position = models.IntegerField()
    job_date_from = models.DateField()
    job_date_to = models.DateField()
    job_location = models.ForeignKey(Address, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.job_company
