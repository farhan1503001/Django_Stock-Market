from django.db import models

# Create your models here.
class Stock(models.Model):
    stock_item=models.CharField(max_length=200)

    def __str__(self):
        return self.stock_item