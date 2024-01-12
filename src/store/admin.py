from django.contrib import admin
from . models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'price',
        'stock',
        'category',
        'created_at',
        'modified_at',
        'is_available',
    )
    prepopulated_fields = {
        'slug': ('product_name',),
    }


# Register your models here.
admin.site.register(Product)