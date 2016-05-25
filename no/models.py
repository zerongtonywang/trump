from django.db import models


class Quote(models.Model):
    quote_text = models.CharField(max_length=256)
    quote_valid = models.BooleanField(default=False)
    quote_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.quote_text


