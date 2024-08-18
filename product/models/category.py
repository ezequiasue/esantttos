# product/models.py

from django.db import models

class Category(models.Model):
    """
    Model representing a product category.
    """
    name = models.CharField(max_length=255)  # Name of the category
    description = models.TextField(blank=True, null=True)  # Optional description for the category
    slug = models.SlugField(unique=True, max_length=255)  # URL-friendly identifier, must be unique
    active = models.BooleanField(default=True)  # Indicates if the category is active

    def __str__(self):
        return self.name  # String representation of the category, showing its name
