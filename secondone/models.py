from django.db import models

# Create your models here.
class second(models.Model):
    productname=models.CharField(max_length=100)
    weight=models.IntegerField()


    def __str__(self):
        return self.productname
