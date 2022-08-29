from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

from products.models import Product, Intro, Events


# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )

# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)



class EventsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(), label='Основные направления')
    training_formats= forms.CharField(widget=CKEditorUploadingWidget(), label='Форма обучения')
    learning_conditions= forms.CharField(widget=CKEditorUploadingWidget(), label='Условия обучения')
    class Meta:
        model = Events
        fields = '__all__'


class IntroInline(admin.TabularInline):
    """Интро на странице фильтра"""
    model = Intro
    extra = 0
    fields = (('name', "draft"), "text_title", ('image', 'get_image'),)
    show_change_link = True
    readonly_fields = ('get_image',)
    verbose_name = 'Добавить интро?'
    verbose_name_plural = 'Добавить интро?'
    # template = 'base.html'
    min_num = 0
    max_num = 2

    def get_image(self, obj, ):
        return mark_safe(f'<img src={obj.image.url} width="100px height=auto">')

    get_image.short_description = "Изображение"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'image', 'get_image', 'power', 'number_of_mode', 'views')
    list_filter = ('product__name',)
    search_fields = ('product__name',)
    list_editable = ('power', 'number_of_mode',)
    prepopulated_fields = {'url': ('name',), }
    save_on_top = True
    actions_on_top = True
    save_as = True
    inlines = [IntroInline]
    readonly_fields = ('get_image',)
    fieldsets = (
        ('Заголовок', {
            'fields': (('name', 'url'),),
            'description': "Обязательно для заполнение."
        }),
        ('Текстовые поля', {
            'fields': (('text', 'description'),),

            'classes': ('collapse', 'wide'),
            'description': "При желании заполните текст."
        }),
        ('Об аппарате', {
            'classes': ('collapse',),
            'fields': ('indications_and_principle_of_operation',
                       ('cartridges', 'results_of_procedures', 'features_of_the_device',),),
            'description': "Укажите доп сведения об аппарате."
        }),
        ('Характеристики', {
            'fields': (('power', 'number_of_mode'),),
            'description': "Укажите характеристики."
        }),

        ('Изображение', {
            'fields': (('image', 'get_image'),),
            'description': ""
        }),
        ('Видео', {
            'fields': (('file',),),
            'description': ""
        }),
    )

    def get_image(self, obj, ):
        return mark_safe(f'<img src={obj.image.url} width="100px height=auto">')

    get_image.short_description = "Изображение"


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'article_date', 'data_up')
    # list_editable = ('article_date',)
    prepopulated_fields = {'url': ('title',), }
    save_on_top = True
    actions_on_top = True
    save_as = True
    form = EventsAdminForm
