from rest_framework import serializers
from order.models.order_item import OrderItem
from product.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    # Use the ProductSerializer to represent the product related to this order item.
    product = ProductSerializer()
    
    # Make the order field read-only and only display its primary key.
    order = serializers.PrimaryKeyRelatedField(read_only=True)  

    class Meta:
        model = OrderItem
        # Specify which fields should be included in the serialized output.
        fields = ('order', 'product', 'quantity', 'price')
