from django.db import models

import re, string

# Create your models here.
class Text(models.Model):
    name = models.CharField(max_length=50, null=True)
    body = models.TextField(null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for word in self.get_body_words():
            Word.objects.create(
                name=word,
            )

    def get_body_words(self):
        str_without_punc = re.sub("[%s]" % re.escape(string.punctuation), "", self.body)
        return str_without_punc.split()


class Word(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=10, default="New")
