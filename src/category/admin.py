from django.contrib import admin
from .models import Category
"""
Super user account:
    username: superuser_1
    password: superuser123456
"""


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('category_name',),
    }
    list_display = (
        'category_name',
        'slug',
    )


# Register your models here.
admin.site.register(Category, CategoryAdmin)
