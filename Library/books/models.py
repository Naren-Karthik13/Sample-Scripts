from django.db import models

# Create your models here.
class Shelf(models.Model):
    shelf_number = models.IntegerField(unique=True)

    def __str__(self):
        return self.shelf_number

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=30)
    shelf = models.ForeignKey('Shelf', on_delete=models.CASCADE, default="blank")  # ✅ allow NULLs

    def __str__(self):
        return self.title
