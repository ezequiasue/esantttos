from rest_framework import serializers
from order.models.order import Order
from order.models.order_item import OrderItem
from order.serializers.order_item_serializer import OrderItemSerializer
from decimal import Decimal

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()  # Custom method to get order items
    total = serializers.SerializerMethodField()  # Custom method to get the total price

    class Meta:
        model = Order
        fields = (
            "user",  # User who placed the order
            "status",  # Status of the order
            "items",  # List of order items
            "total",  # Total price of the order
            "created_at",  # Timestamp when the order was created
            "updated_at",  # Timestamp when the order was last updated
        )

    def get_items(self, instance):
        """
        Retrieves all order items related to the order instance and serializes them.
        """
        order_items = instance.order_items.all()  # Use the related name defined by Django
        return OrderItemSerializer(order_items, many=True).data

    def get_total(self, instance):
        """
        Calculates the total price of all items in the order.
        """
        order_items = instance.order_items.all()  # Use the related name defined by Django
        total = sum(item.price * item.quantity for item in order_items)
        return str(total)  # Return total as a string for consistency with tests
