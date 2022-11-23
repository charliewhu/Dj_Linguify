from django.db import models


# Create your models here.
class Text(models.Model):
    name = models.CharField(max_length=50, null=True)
    body = models.TextField(null=True)


class Word(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
