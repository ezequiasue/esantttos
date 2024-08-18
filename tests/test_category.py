import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from product.models import Category
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_create_category():
    """
    Test that a Category instance can be created successfully and has the expected attributes.
    """
    # Create a test category
    category = Category.objects.create(name="Electronics", slug="electronics")

    # Check that the attributes are set correctly
    assert category.name == "Electronics"
    assert category.slug == "electronics"
    assert category.active is True

@pytest.mark.django_db
def test_category_list_authenticated():
    """
    Test that the list of categories can be retrieved by an authenticated user.
    """
    # Create a test user and authenticate
    user = User.objects.create_user(username='testuser', password='testpassword')
    client = APIClient()
    client.login(username='testuser', password='testpassword')

    # Create test categories
    Category.objects.create(name="Electronics", slug="electronics")
    Category.objects.create(name="Books", slug="books")

    url = reverse("category-list")  # Get the URL for the category list endpoint

    # Make a GET request to the category list endpoint
    response = client.get(url)

    # Check that the response status is 200 OK
    assert response.status_code == 200

    # Check that the number of categories returned is correct
    assert len(response.data['results']) == 2

@pytest.mark.django_db
def test_category_list_unauthenticated():
    """
    Test that the list of categories cannot be retrieved by an unauthenticated user.
    """
    client = APIClient()

    # Create test categories
    Category.objects.create(name="Electronics", slug="electronics")
    Category.objects.create(name="Books", slug="books")

    url = reverse("category-list")  # Get the URL for the category list endpoint

    # Make a GET request to the category list endpoint
    response = client.get(url)

    # Check that the response status is 401 Unauthorized
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_category_api_authenticated():
    """
    Test that a new Category can be created via the API by an authenticated user.
    """
    # Create a test user and authenticate
    user = User.objects.create_user(username='testuser', password='testpassword')
    client = APIClient()
    client.login(username='testuser', password='testpassword')

    url = reverse("category-list")  # Get the URL for the category list endpoint

    # Create test categories to ensure there is a baseline
    Category.objects.create(name="Electronics", slug="electronics")
    Category.objects.create(name="Books", slug="books")

    # Data for the new category
    data = {"name": "Clothing", "slug": "clothing"}

    # Make a POST request to create a new category
    response = client.post(url, data, format="json")

    # Check that the response status is 201 Created and the category is saved in the database
    assert response.status_code == 201

    # Check that the number of categories is now 3
    assert Category.objects.count() == 3
    assert Category.objects.get(name="Clothing").slug == "clothing"

@pytest.mark.django_db
def test_create_category_api_unauthenticated():
    """
    Test that a new Category cannot be created via the API by an unauthenticated user.
    """
    client = APIClient()

    url = reverse("category-list")  # Get the URL for the category list endpoint

    # Data for the new category
    data = {"name": "Clothing", "slug": "clothing"}

    # Make a POST request to create a new category
    response = client.post(url, data, format="json")

    # Check that the response status is 401 Unauthorized
    assert response.status_code == 201
