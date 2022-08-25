from django.urls import path

from products.views import ProductHomeView, ProductCatalog, ProductDetailView

urlpatterns = [
    path('', ProductHomeView.as_view(), name='home'),
    path('catalog/', ProductCatalog.as_view(), name='catalog'),
    path('<slug:slug>', ProductDetailView.as_view(), name='product_detail')
]
