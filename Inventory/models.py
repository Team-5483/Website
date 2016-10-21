from django.db import models


# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_reference = models.CharField(max_length=50)
    item_source = models.CharField(max_length=50)
    item_quantity = models.IntegerField(max_length=50)
    item_measurement = models.CharField(max_length=50)
    item_unit_price = models.IntegerField(max_length=50)
    item_total_price = models.IntegerField(max_length=50)

    def save(self, *args, **kwargs):
       # if(self.item_quantity != None & self.item_unit_price != None) :
        self.item_total_price = self.item_quantity * self.item_unit_price
        super(Item, self).save(*args, **kwargs)
