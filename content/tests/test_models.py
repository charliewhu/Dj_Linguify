from django.test import TestCase

from .factory import TextFactory

from ..models import Word


class TextTest(TestCase):
    def setUp(self):
        self.text_body = "test text body."
        self.text = TextFactory(body=self.text_body)

    def test_words_created(self):
        """
        a word should be creared for each word in the Text body,
        with status = "new"
        """
        self.assertEqual(Word.objects.count(), len(self.text_body.split()))
        self.assertEqual(Word.objects.first().name, "test")
        self.assertEqual(Word.objects.first().status, "new")
        self.assertEqual(Word.objects.last().name, "body")

    def test_duplicate_words_not_created(self):
        """
        if a Word already exists,
        do not create new objects,
        do not change status of existing object
        """
        # add new text with word crossover
        pass
