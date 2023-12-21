from django.contrib import admin

from pages.models import HomeProductsModel, PostsModel


@admin.register(HomeProductsModel)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    search_fields = ['title', 'price']


@admin.register(PostsModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'job']
    search_fields = ['name', 'job']