from django.db import models

# Create your models here

class PurchaseCategory(models.Model):
    name = models.CharField(max_length=100)
    carbon_footprint_per_unit = models.FloatField()  # kg CO2 per unit

    def __str__(self):
        return self.name

class Purchase(models.Model):
    category = models.ForeignKey(PurchaseCategory, on_delete=models.CASCADE)
    amount = models.FloatField()  # Quantity of the item
    date = models.DateField(auto_now_add=True)

    def carbon_footprint(self):
        return self.amount * self.category.carbon_footprint_per_unit
