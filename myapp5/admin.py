from django.contrib import admin
from .models import Category, Product


@admin.action(description='Сбросить количество в ноль')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']
    list_filter = ['date_add', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (desription)'
    actions = [reset_quantity]

    """Отдельный продукт"""
    # fields = ['name', 'description', 'category']
    readonly_fields = ['date_add', 'rating']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields':['category', 'description'],
        },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['rating', 'date_addсв'],
            }
        ),
    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
