import pytest
from product.models.category import Category
from product.models.product import Product

@pytest.mark.django_db
def test_create_category():
    """
    Test that a Category can be created with correct attributes.
    """
    # Create a test category
    category = Category.objects.create(name="Electronics", slug="electronics")
    
    # Check the category attributes
    assert category.name == "Electronics"  # Verify the name of the category
    assert category.slug == "electronics"  # Verify the slug of the category
    assert category.active is True  # Ensure the category is active by default

@pytest.mark.django_db
def test_create_product():
    """
    Test that a Product can be created and associated with a Category.
    """
    # Create a test category
    category = Category.objects.create(name="Electronics", slug="electronics")
    
    # Create a test product and assign the category
    product = Product.objects.create(
        name="Smartphone",
        description="A high-end smartphone.",
        price=999.99,  # Price as a float for simplicity
        stock=10,
        active=True,
        category=category  # Assign the category to the product
    )
    
    # Check the product attributes
    assert product.name == "Smartphone"  # Verify the name of the product
    assert product.price == 999.99  # Verify the price of the product
    assert product.category == category  # Verify that the category was assigned correctly
