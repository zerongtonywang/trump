from django.contrib import admin
from .models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('quote_text', 'quote_valid')


admin.site.register(Quote, QuoteAdmin)
