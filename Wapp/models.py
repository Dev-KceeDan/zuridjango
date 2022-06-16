from django.db import models

# Create your models here.

class Schools(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=70)
    # email = models.EmailField(max_length=100)
    # password = models.CharField(max_length=100)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
           return self.name

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
           return self.name