from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

import random

from no.models import Quote
from no.forms import QuoteForm


def index_views(request):
    context = {}
    quote = random_quote_text()
    context['quote'] = quote.quote_text
    context['likes'] = quote.quote_likes
    return render(request, 'index.html', context)


def add(request):
    context = {}
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your response has been added")
            return HttpResponseRedirect(reverse('no:index'))

    form = QuoteForm()
    context["form"] = form

    return render(request, 'add.html', context)


def random_quote_text():
    quotes = Quote.objects.filter(quote_valid=True)
    quote = random.choice(quotes)
    return quote
