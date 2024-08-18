from rest_framework import serializers
from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer  # Import the CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    """
    category = CategorySerializer()  # Use CategorySerializer to serialize the category

    class Meta:
        model = Product  # Specify that this serializer is for the Product model
        fields = (
            "id",  # The ID field of the product
            "name",  # The name field of the product
            "description",  # The description field of the product
            "price",  # The price field of the product
            "stock",  # The stock field of the product
            "active",  # The active field indicating if the product is active or not
            "category",  # The category field, serialized using CategorySerializer
        )
        extra_kwargs = {
            'price': {'required': False},  # The price field is not required
            'active': {'required': False},  # The active field is not required
            'category': {'required': True}  # The category field is required
        }
