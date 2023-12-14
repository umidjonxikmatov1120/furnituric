from django.shortcuts import render


def home_page_view(request):
    return render(request, template_name='home.html')


def contact_page_view(request):
    return render(request, template_name='contact.html')


def about_us_view(request):
    return render(request, template_name='about-us.html')


def product_list_view(request):
    return render(request, template_name='product-list.html')