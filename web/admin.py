from django.contrib import admin
from .models import Product,Customer
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'description', 'price', 'stock']
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display =  ['name', 'last_name', 'age', 'email','phone']
    