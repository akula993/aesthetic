from django import template
from django.db.models import Sum

from products.models import Product

register = template.Library()


@register.simple_tag
def get_popular_articles_for_week():
    popular = Product.objects.filter.values(
        # Забираем интересующие нас поля, а именно id и заголовок
        # К сожалению забрать объект по внешнему ключу в данном случае не получится
        # Только конкретные поля из объекта
        'product_id', 'product__name',
    ).annotate(
        # Суммируем записи по просмотрам
        sum_views=Sum('views')
    ).order_by(
        # отсортируем записи по убыванию
        '-sum_views')[:5]  # Заберём последние пять записей

    return popular