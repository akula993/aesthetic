from django.contrib import admin

from products.models import Product, Intro


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',), }
    save_on_top = True
    actions_on_top = True
    save_as = True


@admin.register(Intro)
class IntroAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'url': ('name',), }
    save_on_top = True
    actions_on_top = True
    save_as = True
