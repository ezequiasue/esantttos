"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from core.views import ProtectedEndpointView, index
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),  # Debug Toolbar URLs (development only)
    path('admin/', admin.site.urls),  # Admin interface
    path('', index, name='index'),  # Root URL mapped to the home view
    path('api/orders/', include('order.urls')),  # Orders API
    path('api/products/', include('product.urls')),  # Products API
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # OpenAPI schema endpoint
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Swagger UI documentation
    path('api/token/', obtain_auth_token, name='obtain-token'),  # URL for obtaining token
    path('api/protected/', ProtectedEndpointView.as_view(), name='protected-endpoint'),  # URL for protected endpoint
]
