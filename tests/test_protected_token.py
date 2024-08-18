import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token

@pytest.mark.django_db
def test_protected_endpoint_with_token():
    # Create a test user
    user = User.objects.create_user(username='testuser', password='testpassword')
    
    # Obtain an authentication token
    client = APIClient()
    response = client.post('/api/token/', {'username': 'testuser', 'password': 'testpassword'})
    
    # Verify that the token was returned successfully
    assert response.status_code == status.HTTP_200_OK
    token = response.data.get('token')
    assert token, "Token not found in response"
    
    # Set up the client with the token for authenticated requests
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    
    # Make an authenticated request to the protected endpoint
    response = client.get('/api/protected/')
    
    # Verify the response status and content
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {"message": "This is a protected endpoint."}
