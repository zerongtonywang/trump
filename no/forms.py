from django import forms
from no.models import Quote


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["quote_text"]
        labels = {
            "quote_text": "Your response"
        }
        error_messages = {
            "quote_text": {
                "required": "Enter a phrase before submitting, how hard is that?"
            }
        }
