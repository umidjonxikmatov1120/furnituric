from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls', namespace="products")),
    path('', include('pages.urls', namespace='home')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)