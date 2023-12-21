from django.db import models


class PostsModel(models.Model):
    long_description = models.TextField()
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"


class HomeProductsModel(models.Model):
    photo1 = models.ImageField(upload_to='products')
    photo2 = models.ImageField(upload_to='products')
    title = models.CharField(max_length=255)
    price = models.FloatField()
    discount_price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "home_product"
        verbose_name_plural = "home_products"
