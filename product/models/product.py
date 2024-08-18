from django.db import models
from decimal import Decimal

class Product(models.Model):
    """
    Model representing a product in the inventory.
    """
    name = models.CharField(max_length=255)  # Name of the product
    description = models.TextField()  # Detailed description of the product
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))  # Price of the product
    stock = models.PositiveIntegerField()  # Quantity available in stock
    active = models.BooleanField(default=True)  # Indicates if the product is active
    category = models.ForeignKey("Category", related_name="products", on_delete=models.CASCADE)  # Related category
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the product was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the product was last updated

    def __str__(self):
        return self.name  # String representation of the product, showing its name
