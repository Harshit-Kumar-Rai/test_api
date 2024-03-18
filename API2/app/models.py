from django.db import models

# Create your models here.
class Company(models.Model):
  company_name = models.CharField(max_length=200)
  username = models.CharField(max_length=64)
  password = models.CharField(max_length=128)
  logo = models.ImageField(upload_to="compnay/logo", blank=True)
  location = models.CharField(max_length=150)
  
  def __str__(self):
    return self.company_name