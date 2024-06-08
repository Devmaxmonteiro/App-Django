from django.contrib import admin

from products import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'brand', 'price',)
    search_filter = ('category', 'brand',)
    
admin.site.register(models.Product, ProductAdmin)

