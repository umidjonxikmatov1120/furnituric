from django.shortcuts import render

from pages.models import *


def home_page_view(request):
    products = HomeProductsModel.objects.all()
    posts = PostsModel.objects.all()
    context = {
        "products": products,
        "posts": posts
    }
    return render(request, template_name='home.html', context=context)


def contact_page_view(request):
    return render(request, template_name='contact.html')


def about_us_view(request):
    return render(request, template_name='about-us.html')


def product_list_view(request):
    return render(request, template_name='product-list.html')