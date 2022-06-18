from django.db import models

# Create your models here.
class Establishment(models.Model):
    
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    canton = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255,blank=True)
    email = models.CharField(max_length=255,blank=True)
    created_time = models.DateTimeField(auto_now_add=True)\
    
    def __str__(self):
        return self.name+" "+self.province