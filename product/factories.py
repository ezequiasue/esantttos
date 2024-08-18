import os
import sys
import django

# Add the project path to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Initialize Django
django.setup()

import factory
from product.models.category import Category
from product.models.product import Product

class CategoryFactory(factory.django.DjangoModelFactory):
    """
    Factory to create instances of Category.
    """
    name = factory.Faker("word")  # Generates a realistic category name
    slug = factory.Faker("slug")  # Generates a realistic slug
    description = factory.Faker("text")  # Generates a realistic description
    active = factory.Iterator([True, False])  # Alternates between True and False

    class Meta:
        model = Category

class ProductFactory(factory.django.DjangoModelFactory):
    """
    Factory to create instances of Product.
    """
    name = factory.Faker("word")  # Generates a realistic product name
    description = factory.Faker("text")  # Generates a realistic product description
    price = factory.Faker("pydecimal", left_digits=4, right_digits=2, positive=True)  # Generates a realistic price
    stock = factory.Faker("pyint")  # Generates a realistic stock quantity
    active = factory.Iterator([True, False])  # Alternates between True and False
    category = factory.SubFactory(CategoryFactory)  # Automatically creates a related Category instance

    class Meta:
        model = Product

if __name__ == "__main__":
    # Create 5 categories and 10 products
    for _ in range(2):
        CategoryFactory()

    for _ in range(2):
        ProductFactory()

    print("Categories and products created successfully!")
    
    
    print(__name__)
