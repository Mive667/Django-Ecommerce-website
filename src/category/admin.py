from django.contrib import admin
from .models import Category
"""
Super user account:
    username: superuser_1
    password: superuser123456
"""

# Register your models here.
admin.site.register(Category)
