from django.shortcuts import render

from products.models import TagModel, ProductModel, CategoryModel, CompanyModel, ColorModel


def tag_view(request):
    tags = TagModel.objects.all()
    context = {
        "tag": tags
    }
    return render(request, template_name="product-list.html", context=context)


def product_view(request):
    products = ProductModel.objects.all()
    company = CompanyModel.objects.all()
    color = ColorModel.objects.all()
    category = CategoryModel.objects.all()
    context = {
        "products": products,
        "companies": company,
        "colors": color,
        "categories": category,
    }
    return render(request, template_name="product-list.html", context=context)


def home_view(request):
    products = HomeProductsModel.objects.all()
    context = {
        "things": products
    }
    return render(request, template_name="home.html", context=context)


def products_page_view(request):
    cat = request.GET.get('cat')
    company = request.Get.get('company')
    color = request.GET.get('color')
    tag = request.GET.get('tag')
    q = request.GET.get('q')

    colors = ColorModel.objects.all().order_by('-pk')
    tags = TagModel.objects.all().order_by('-pk')
    companies = CompanyModel.objects.all().order_by('-pk')
    products = ProductModel.objects.all().order_by('-pk')
    categories = CategoryModel.objects.all().order_by('-pk')

    if cat:
        products = products.filter(categories=cat)
    elif color:
        products = products.filter(categories=color)
    elif tag:
        products = products.filter(categories=tag)
    elif company:
        products = products.filter(categories=company)
    elif q:
        products = products.filter(title__icontains=q)

    context = {
        "products": products,
        "categories": categories,
        "tags": tags,
        "companies": companies,
        "colors": colors
    }
    return render(request, template_name="product_filter.html", context=context)


def post_view(request):
    posts = PostsModel.objects.all()
    context = {
        "posts": posts
    }
    return render(request, template_name="home.html", context=context)
