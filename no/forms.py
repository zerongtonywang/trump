from django import forms
from no.models import Quote


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["quote_text"]
