from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Unit(models.Model):
    # fill later
    unit_name = models.CharField(max_length=30)

    class Meta:
        ordering = ["unit_name"]

    def __str__(self):
        return self.unit_name

class Ingredient(models.Model):
    # fill later
    ingredient_name = models.CharField(max_length=30)
    quantity = models.DecimalField(max_digits=4, decimal_places=2)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["ingredient_name"]

    def __str__(self):
        return self.ingredient_name

class Recipe(models.Model):
    # fill later
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient)
    directions = models.TextField()
    completion_time = models.DurationField(null=True, blank=True)
    pub_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ["pub_date"]

    def __str__(self):
        return self.recipe_name