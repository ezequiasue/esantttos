import pytest
from rest_framework.exceptions import ValidationError
from product.models.category import Category
from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer
from product.serializers.product_serializer import ProductSerializer

@pytest.mark.django_db
def test_category_serializer_valid_data():
    """
    Test that CategorySerializer correctly serializes valid Category data.
    """
    # Create a test category
    category = Category.objects.create(
        name="Electronics",
        slug="electronics",
        description="Devices and gadgets"
    )
    
    # Serialize the category instance
    serializer = CategorySerializer(category)
    data = serializer.data
    
    # Validate serialized data
    assert data['name'] == "Electronics"  # Verify the name of the category
    assert data['slug'] == "electronics"  # Verify the slug of the category
    assert data['description'] == "Devices and gadgets"  # Verify the description of the category
    assert data['active'] is True  # Ensure the category is active

@pytest.mark.django_db
def test_product_serializer_valid_data():
    """
    Test that ProductSerializer correctly serializes valid Product data.
    """
    # Create a test category
    category = Category.objects.create(
        name="Electronics",
        slug="electronics",
        description="A category for electronics"
    )
    
    # Create a test product and assign the category
    product = Product.objects.create(
        name="Smartphone",
        description="A high-end smartphone.",
        price=999.99,
        stock=10,
        active=True,
        category=category
    )
    
    # Serialize the product instance
    serializer = ProductSerializer(product)
    data = serializer.data
    
    # Validate serialized data
    assert data['name'] == "Smartphone"  # Verify the name of the product
    assert data['price'] == "999.99"  # Verify the price of the product (as a string)
    assert data['category']['id'] == category.id  # Verify the ID of the category
    assert data['category']['name'] == category.name  # Verify the name of the category
    assert data['category']['slug'] == category.slug  # Verify the slug of the category

@pytest.mark.django_db
def test_category_serializer_invalid_data():
    """
    Test that CategorySerializer returns errors for invalid data.
    """
    # Test serializer with invalid data
    serializer = CategorySerializer(data={})
    assert not serializer.is_valid()  # Ensure the serializer is invalid
    assert 'name' in serializer.errors  # Check for error on 'name' field
    assert 'slug' in serializer.errors  # Check for error on 'slug' field

@pytest.mark.django_db
def test_product_serializer_invalid_data():
    """
    Test that ProductSerializer returns errors for invalid data.
    """
    # Test serializer with invalid data
    serializer = ProductSerializer(data={})
    assert not serializer.is_valid()  # Ensure the serializer is invalid
    assert 'name' in serializer.errors  # Check for error on 'name' field
    assert 'category' in serializer.errors  # Check for error on 'category' field
    assert 'description' in serializer.errors  # Check for error on 'description' field
    assert 'stock' in serializer.errors  # Check for error on 'stock' field
    # We don't check 'price' here because it's optional
