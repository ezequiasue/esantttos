from rest_framework import serializers
from product.models.category import Category  # Import the Category model

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """
    class Meta:
        model = Category  # Specify that this serializer is for the Category model
        fields = [
            "id",  # The ID field of the category
            "name",  # The name field of the category
            "description",  # The description field of the category
            "slug",  # The slug field of the category
            "active",  # The active field indicating if the category is active or not
        ]

    def validate_name(self, value):
        """
        Validate that the category name has at least 3 characters.
        """
        if len(value) < 3:  # Check if the name length is less than 3 characters
            raise serializers.ValidationError("The name must be at least 3 characters long.")  # Raise a validation error if the condition is met
        return value  # Return the validated name
