from django.db import models

# Create your models here.
class Collection(models.Model):
    category = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    name=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    quantity=models.IntegerField()
    collection=models.ForeignKey(Collection, on_delete=models.CASCADE)
    def __str__(self):
        return self.name