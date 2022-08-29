from django.contrib.flatpages.views import flatpage
from django.urls import path, include, re_path

from products.views import ProductHomeView, ProductCatalog, ProductDetailView, VideoProduct, EventsViews, \
    EventsDetailView, PartnersViews, PartnerDetailView

urlpatterns = [
    path('stream/<int:pk>/', VideoProduct.get_streaming_video, name='stream'),
    path('', ProductHomeView.as_view(), name='home'),
    path('partner/', PartnersViews.as_view(), name='partner'),
    path('partner/<slug:slug>', PartnerDetailView.as_view(), name='partner_detail'),
    path('catalog/', ProductCatalog.as_view(), name='catalog'),

    path('catalog/<slug:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('events/', EventsViews.as_view(), name='events'),
    # re_path(r'^(?P<url>.*/)$', flatpage),
    path('about-us/', flatpage, {'url': '/pages/about-us/'}, name='about'),
    path('matherials/', flatpage, {'url': '/pages/matherials/'}, name='matherials'),
    path('events/<slug:slug>', EventsDetailView.as_view(), name='event_detail'),
]
