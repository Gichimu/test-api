from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name

class Order(models.Model):
    items = models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.quantity} of {self.item.name}'