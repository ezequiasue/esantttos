import pytest
from django.contrib.auth.models import User
from order.models import Order, OrderItem
from product.models import Product, Category
from decimal import Decimal

@pytest.mark.django_db
def test_create_order():
    """
    Test that an Order can be created with associated OrderItems.
    """
    # Create a test user
    user = User.objects.create_user(
        username="testuser", email="test@example.com", password="password"
    )

    # Create a test category
    category = Category.objects.create(name="Electronics", slug="electronics")

    # Create a test product and associate it with the category
    product = Product.objects.create(
        name="Smartphone",
        description="A high-end smartphone.",
        price=Decimal("999.99"),
        stock=10,
        active=True,
        category=category
    )

    # Create a test order for the user
    order = Order.objects.create(user=user, status="pending")

    # Add an item to the order
    order_item = OrderItem.objects.create(
        order=order,
        product=product,
        quantity=2,
        price=product.price
    )

    # Assertions to verify the order was created correctly
    assert order.user == user
    assert order.status == "pending"
    assert order.order_items.count() == 1
    assert order.order_items.first() == order_item
    assert order.order_items.first().product == product
    assert order.order_items.first().quantity == 2
    assert order.order_items.first().price == Decimal(product.price)

@pytest.mark.django_db
def test_order_item_creation():
    """
    Test that an OrderItem can be created with the correct attributes.
    """
    # Create a test user
    user = User.objects.create_user(
        username="testuser", email="test@example.com", password="password"
    )

    # Create a test category
    category = Category.objects.create(name="Electronics", slug="electronics")

    # Create a test product and associate it with the category
    product = Product.objects.create(
        name="Smartphone",
        description="A high-end smartphone.",
        price=Decimal("999.99"),
        stock=10,
        active=True,
        category=category
    )

    # Create a test order for the user
    order = Order.objects.create(user=user, status="pending")

    # Add an item to the order
    order_item = OrderItem.objects.create(
        order=order,
        product=product,
        quantity=2,
        price=product.price
    )

    # Assertions to verify the order item was created correctly
    assert order_item.order == order
    assert order_item.product == product
    assert order_item.quantity == 2
    assert order_item.price == Decimal(product.price)
