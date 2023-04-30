from django.db import models

# Create your models here.

# First model(Item)


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
    # gives the items actual names
    def __str__(self):
        return self.name
