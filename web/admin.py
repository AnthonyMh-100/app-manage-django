from django.contrib import admin
from .models import Product
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ['name', 'description', 'price', 'stock']
    