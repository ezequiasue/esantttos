from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user who placed the order
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")  # Status of the order
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the order was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the order was last updated

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"  # String representation of the order
