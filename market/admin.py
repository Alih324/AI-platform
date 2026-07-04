from django.contrib import admin

from .models import Product, Product_Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price', 'found', 'created_at')
    search_fields = ('product_name', 'category', 'details')
    list_filter = ('category', 'found', 'created_at')
    list_editable = ('found',)
    ordering = ('-created_at',)


@admin.register(Product_Review)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'rating', 'created_at')
    search_fields = ('product__product_name', 'author__username', 'content')
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',)
