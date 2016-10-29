from django.db import models


# Create your models here.
class Item(models.Model):
    item_categories = ['None', 'Pneumatic' , 'Electrical', 'Mechanical']
    item_category = models.CharField(max_length=20,default='None')
    item_name = models.CharField(max_length=50)
    item_reference = models.CharField(max_length=50)
    item_source = models.CharField(max_length=50)
    item_quantity = models.CharField(max_length=50,default='0')
    item_measurement = models.CharField(max_length=50)
    item_unit_price = models.CharField(max_length=50, default='0')
    item_total_price = models.FloatField(max_length=50)
    item_field_names = ['item_name', 'item_reference', 'item_source', 'item_quantity', 'item_measurement',
                        'item_unit_price', 'item_total_price']

    def save(self, *args, **kwargs):
        self.item_total_price = float(self.item_quantity) * float(self.item_unit_price)
        super(Item, self).save(*args, **kwargs)
