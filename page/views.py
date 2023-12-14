from django.shortcuts import render

from page.models import TagModel, ProductModel


def tag_view(request):
    tags = TagModel.objects.all()
    context = {
        "tag": tags
    }
    return render(request, template_name="product-list.html", context=context)


def product_view(request):
    products = ProductModel.objects.all()
    context = {
        "product": products
    }
    return render(request, template_name="product-list.html", context=context)
