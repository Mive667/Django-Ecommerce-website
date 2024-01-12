from django.contrib import admin
from . models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'category',
        'price',
        'stock',
        'is_available',
        'created_at',
        'modified_at',   
    )
    prepopulated_fields = {
        'slug': ('product_name',),
    }


# Register your models here.
admin.site.register(Product, ProductAdmin)
