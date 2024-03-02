from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ingredient Name')
    quantity = models.DecimalField(max_digits=9, decimal_places=1, verbose_name="Ingredient Quantity")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Ingredient Price")

class MenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name='Menu Item Name')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Menu Item Price')

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, verbose_name='Related Menu Item')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, verbose_name='Ingredient')
    quantity = models.DecimalField(max_digits=6, decimal_places=1, verbose_name="Required Quantity")

class Purchase(models.Model):
    customer_name = models.CharField(max_length=100, verbose_name='Customer Name')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, verbose_name='Purchased Menu Item')
    purchase_date = models.DateTimeField(verbose_name='Purchase Date')