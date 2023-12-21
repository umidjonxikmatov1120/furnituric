from django.urls import path

from .views import product_view, home_view

app_name = 'products'

urlpatterns = [
    path('product/', product_view, name='product'),
    path('home/', home_view, name='home')
]