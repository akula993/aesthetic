import datetime
import fnmatch
import os

from django.utils.timezone import now
from django.conf import settings
from django.db.models import F
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, DetailView

from products.models import Product, Intro, Events, Partners
from products.services import open_file


class VideoProduct:
    def get_streaming_video(request, pk: int):
        file, status_code, content_length, content_range = open_file(request, pk)
        response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

        response['Accept-Ranges'] = 'bytes'
        response['Content-Length'] = str(content_length)
        response['Cache-Control'] = 'no-cache'
        response['Content-Range'] = content_range
        return response


class IntroViews:
    """Жанры и года выхода фильмов"""

    def get_genres(self):
        return Intro.objects.filter(draft=True)


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


class ProductDetailView(VideoProduct, DetailView):
    model = Product
    template_name = 'product/product.html'
    # context_object_name = 'product'
    slug_field = 'url'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_section(self, obj):
        content = Product.objects.filter(object != None)
        return content


class EventsViews(ListView):
    model = Events
    template_name = 'product/events/events.html'
    context_object_name = 'events'
    slug_field = 'url'
    extra_context = {'title': 'Мероприятия'}

    # def get_queryset(self):
    #     now = timezone.now()
    #     upcoming = Events.objects.filter(article_date__gte=now).order_by('article_date')
    #     passed = Events.objects.filter(article_date__lt=now).order_by('-article_date')
    #     return list(upcoming) + list(passed)

    # def get_queryset(self):
    #     now = timezone.now()
    #     upcoming = Events.objects.filter(article_date__gte=now).order_by('article_date')
    #     passed = Events.objects.filter(article_date__lt=now).order_by('-article_date')
    #     return list(upcoming) + list(passed)


class EventsDetailView(DetailView):
    model = Events
    template_name = 'product/events/event.html'
    context_object_name = 'event'
    slug_field = 'url'
    extra_context = {'title': 'Мероприятия'}

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class PartnersViews(ListView):
    model = Partners
    template_name = 'partners.html'
    context_object_name = 'partners'
    slug_field = 'url'
    extra_context = {'title': 'Партнеры'}

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prod_comp'] = Product.objects.all()
        return context

class PartnerDetailView(DetailView):
    model = Partners
    template_name = 'partner.html'
    context_object_name = 'partner'
    slug_field = 'url'
    extra_context = {'title': 'Партнеры'}

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
