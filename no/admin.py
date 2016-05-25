from django.contrib import admin
from .models import Quote


def mark_valid(modeladmin, request, queryset):
    queryset.update(quote_valid=True)


def mark_invalid(modeladmin, request, queryset):
    queryset.update(quote_valid=False)


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('quote_text', 'quote_valid')
    actions = [mark_valid, mark_invalid]


admin.site.register(Quote, QuoteAdmin)
