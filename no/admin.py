from django.contrib import admin

# Register your models here.
from .models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('quote_text', 'quote_valid')
    list_filter = ('quote_text', 'quote_valid')


admin.site.register(Quote, QuoteAdmin)
