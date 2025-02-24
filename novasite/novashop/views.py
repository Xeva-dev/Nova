from django.shortcuts import render, get_object_or_404  # Fixed missing import
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status  # Fixed missing import
from .models import Products, Order
from .serializers import ProductSerializer

# API to get all products or add a new product
@api_view(['GET', 'POST'])
def get_products(request):
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API to get, update, or delete a single product
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):
    product = get_object_or_404(Products, id=id)  # Fixed missing import

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Homepage view
def index(request):
    product_objects = Products.objects.all()

    # Search functionality
    item_name = request.GET.get('item_name')
    if item_name:
        product_objects = product_objects.filter(title__icontains=item_name)

    # Pagination
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    
    return render(request, 'shop/index.html', {'product_objects': product_objects})

# Product detail page
def detail(request, id):
    product_object = get_object_or_404(Products, id=id)  # Used get_object_or_404 for error handling
    return render(request, 'shop/detail.html', {'product_object': product_object})

# Checkout view
def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zipcode = request.POST.get('zipcode', "")
        total = request.POST.get('total', "")
        
        order = Order(
            items=items,
            name=name,
            email=email,
            address=address,
            city=city,
            state=state,
            zipcode=zipcode,
            total=total
        )
        order.save()

    return render(request, 'shop/checkout.html')
