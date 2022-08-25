from django.db.models import F
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from products.models import Product


class ProductHomeView(ListView):
    model = Product
    template_name = 'product/home.html'
    context_object_name = 'products'
    extra_context = {'title': 'Главная'}


class ProductCatalog(ListView):
    model = Product
    template_name = 'product/catalog.html'
    context_object_name = 'products'
    extra_context = {'title': 'Каталог',
                     'name': 'Аппарат',
                     'about': 'Краткое описание продукции компании. Воплощение стиля и технологий. '
                              'Тысячи приложений, голосовой поиск и мгновенная загрузка контента'}


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product.html'
    context_object_name = 'product'
    slug_field = 'url'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
