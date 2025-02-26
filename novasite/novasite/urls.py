"""
URL configuration for novasite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, re_path
from novashop.views import get_products, product_detail, index, detail, checkout  # Corrected import

# Import drf-yasg for API documentation
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# Schema view for Swagger documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Product API",
        default_version='v1',
        description="API documentation for managing products",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('<int:id>/', detail, name='detail'),
    path('checkout/', checkout, name='checkout'),
    
    # API Endpoints
    path('api/products/', get_products, name='api-products'),  # GET & POST
    path('api/products/<int:id>/', product_detail, name='api-product-detail'),  # GET, PUT, DELETE

    # Swagger documentation
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
