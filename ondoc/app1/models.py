from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    qty=models.IntegerField()
    description=models.TextField()
    color=models.CharField(max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        db_table="product"