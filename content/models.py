from django.db import models

import re, string


class Word(models.Model):
    name = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=10, default="New")

    def __str__(self):
        return self.name


class Text(models.Model):
    name = models.CharField(max_length=50, null=True)
    body = models.TextField(null=True)
    words = models.ManyToManyField(Word, through="TextWord")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.create_words_from_body()

    def create_words_from_body(self):
        for word in self.get_body_words():
            word_obj = Word.objects.get_or_create(
                name=word,
            )

            TextWord.objects.create(
                word=word_obj[0],
                text=self,
            )

    def get_body_words(self):
        str_without_punc = re.sub("[%s]" % re.escape(string.punctuation), "", self.body)
        return str_without_punc.split()


class TextWord(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    text = models.ForeignKey(Text, on_delete=models.CASCADE)
