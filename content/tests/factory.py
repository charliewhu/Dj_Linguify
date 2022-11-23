from factory.django import DjangoModelFactory
from factory import SubFactory


class TextFactory(DjangoModelFactory):
    class Meta:
        model = "content.Text"

    name = "test Text"
    body = "test Body"
