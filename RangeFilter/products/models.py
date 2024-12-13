from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    size = models.CharField(max_length=50)  
    
    def __str__(self):
        return self.name
