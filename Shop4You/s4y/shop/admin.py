from django.contrib import admin

# Register your models here.
from .models import Product,Contact, OrderUpdate
from .models import Order
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(OrderUpdate)