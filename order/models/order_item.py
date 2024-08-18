# order/models/order_item.py
from django.db import models
from order.models import Order
from product.models import Product

class OrderItem(models.Model):
    # Links each OrderItem to an Order. Deleting an order will also delete related OrderItems.
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    
    # Links each OrderItem to a Product.
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    # Stores the quantity of the product ordered.
    quantity = models.PositiveIntegerField()
    
    # Stores the price of the product for this order item.
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        # Returns a string representation of the OrderItem, showing quantity, product name, and order ID.
        return f"{self.quantity} x {self.product.name} for Order {self.order.id}"
