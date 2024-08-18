import os
import sys
import django

# Add the project's directory to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Initialize Django
django.setup()

import factory
from django.contrib.auth.models import User
from order.models import Order
from product.factories import ProductFactory
from order.models import OrderItem

class UserFactory(factory.django.DjangoModelFactory):
    """
    Factory to create instances of User.
    """
    email = factory.Faker("email")
    username = factory.Faker("user_name")
    password = factory.PostGenerationMethodCall('set_password', 'password123')

    class Meta:
        model = User

class OrderFactory(factory.django.DjangoModelFactory):
    """
    Factory to create instances of Order.
    """
    user = factory.SubFactory(UserFactory)  # Creates an associated user

    @factory.post_generation
    def items(self, create, extracted, **kwargs):
        """
        Adds OrderItems to an order after it is created.
        """
        if not create:
            return

        if extracted:
            for product, quantity, price in extracted:
                OrderItem.objects.create(order=self, product=product, quantity=quantity, price=price)

    class Meta:
        model = Order

# Execute the script to create an order with items
if __name__ == "__main__":
    from product.factories import ProductFactory

    # Create some products
    products = ProductFactory.create_batch(3)  # Creates 3 products

    # Create an order and associate these products with quantities and prices
    items = [(product, 2, 19.99) for product in products]  # Example: 2 units of each product, price 19.99
    order = OrderFactory(items=items)
    print(order)
