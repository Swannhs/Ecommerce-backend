from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ecommerce.products import products


@api_view(['GET'])
def allProducts(request):
    return Response(products)
