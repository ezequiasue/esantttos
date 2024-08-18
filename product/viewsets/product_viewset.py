from rest_framework.viewsets import ModelViewSet
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework.permissions import AllowAny

class ProductViewSet(ModelViewSet):
    """
    ViewSet for handling CRUD operations on Product objects.
    """
    queryset = Product.objects.all().order_by('id')  # Queryset to retrieve all Product objects, ordered by 'id'
    serializer_class = ProductSerializer  # Serializer for Product objects

    # authentication_classes = [BasicAuthentication, SessionAuthentication]  # Authentication methods used
    permission_classes = [AllowAny]  # Not required permissions
