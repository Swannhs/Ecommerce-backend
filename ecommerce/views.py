from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ecommerce.models import Product
from ecommerce.serailizers import ProductSerializer


@api_view(['GET'])
def allProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
