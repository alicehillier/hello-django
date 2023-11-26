from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False) 
    done = models.BooleanField(null=False, blank=False, default=False)

# The code below ensures the todo item's name is displayed
    def __str__(self):
        return self.name
        