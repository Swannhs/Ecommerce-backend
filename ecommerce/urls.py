from django.urls import path

from ecommerce import views

urlpatterns = [
    path('api/products/', views.allProducts, name='Items'),
    path('api/products/<str:id>/', views.detailsProduct, name='Item'),
]
