from rest_framework.viewsets import ModelViewSet
from product.models import Category
from product.serializers import CategorySerializer
from rest_framework.permissions import AllowAny

class CategoryViewSet(ModelViewSet):
    """
    ViewSet for handling CRUD operations on Category objects.
    """
   
    queryset = Category.objects.all()# Queryset to retrieve all Order objects
    serializer_class = CategorySerializer # Serializer for Order objects
    
    #authentication_classes = [BasicAuthentication, SessionAuthentication]  # Authentication methods used
    permission_classes = [AllowAny]  # Not Required permissions
    
  