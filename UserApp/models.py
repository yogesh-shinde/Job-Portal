from django.db import models
from phone_field import PhoneField
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    conform_password = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    contact = PhoneField(help_text='Contact phone number')
    resume = models.FileField(upload_to='files')
    
    def __str__(self):
        return self.name
