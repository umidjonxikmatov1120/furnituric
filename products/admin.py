from django.contrib import admin

from products.models import CategoryModel, ColorModel, ProductModel, CompanyModel, TagModel, ProductImageModel


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


class ProductImageModelAdmin(admin.StackedInline):
    model = ProductImageModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    search_fields = ['title', 'price']
    inlines = [ProductImageModelAdmin]


@admin.register(TagModel)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


