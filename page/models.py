from django.db import models


class CategoryModel(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class CompanyModel(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'


class TagModel(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class ColorModel(models.Model):
    color = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'


class ProductModel(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='product')
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    price = models.FloatField()
    is_stock = models.BooleanField(default=True)

    category = models.ManyToManyField(CategoryModel, related_name="products")
    tags = models.ManyToManyField(TagModel, related_name="products")
    color = models.ManyToManyField(ColorModel, related_name="products")
    companies = models.ManyToManyField(CompanyModel, related_name="products")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

