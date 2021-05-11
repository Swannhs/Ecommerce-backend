from django.contrib import admin

# Register your models here.
from ecommerce.models import Product, Review, Order, ShippingAddress

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(ShippingAddress)