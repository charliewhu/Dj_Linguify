from django.test import TestCase

from .factory import TextFactory

from ..models import Text, TextWord, Word


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
        self.assertEqual(Word.objects.first().status, "New")
        self.assertEqual(Word.objects.last().name, "body")

    def test_get_body_words(self):
        words = self.text.get_body_words()
        self.assertEqual(
            words,
            [
                "test",
                "text",
                "body",
            ],
        )

    def test_duplicate_words_not_created(self):
        """
        if a Word already exists,
        do not create new objects,
        do not change status of existing object
        """
        # add new text with word crossover
        TextFactory(body="test")
        self.assertEqual(Word.objects.count(), 3)

    def test_manytomany_relation_created(self):
        self.assertEqual(self.text.words.count(), 3)
        self.assertEqual(TextWord.objects.count(), 3)
