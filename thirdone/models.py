from django.db import models

# Create your models here.
class third(models.Model):
    prdct=models.CharField(max_length=100)
    wt=models.IntegerField()

    def __str__(self):
        return self.prdct
