from django.urls import path

from products.views import ProductHomeView, ProductCatalog, ProductDetailView, VideoProduct, EventsViews, EventsDetailView

urlpatterns = [
    path('stream/<int:pk>/', VideoProduct.get_streaming_video, name='stream'),
    path('', ProductHomeView.as_view(), name='home'),
    path('catalog/', ProductCatalog.as_view(), name='catalog'),
    path('catalog/<slug:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('events/', EventsViews.as_view(), name='events'),
    path('events/<slug:slug>', EventsDetailView.as_view(), name='event_detail'),
]
