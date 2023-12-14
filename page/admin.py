from django.contrib import admin

from page.models import CategoryModel, ColorModel, ProductModel, CompanyModel, TagModel


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(CompanyModel)
class ManufactoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(ColorModel)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['color', 'code']
    search_fields = ['color', 'code']


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    search_fields = ['title', 'price']


@admin.register(TagModel)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

