from django.contrib import admin
from .models import StockItem, Category

admin.site.register(StockItem)
admin.site.register(Category)