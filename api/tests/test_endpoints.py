from rest_framework.test import APITestCase

from content.tests.factory import TextFactory


class TextDetailTest(APITestCase):
    def setUp(self):
        self.url = "/api/texts/1/"
        self.text = TextFactory()

    def test_GET(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            res.data,
            {
                "id": self.text.id,
                "name": self.text.name,
                "body": self.text.body,
            },
        )


class TextWordDetailTest(APITestCase):
    def setUp(self):
        self.url = "/api/text_words/1/"
        self.body = "test"
        self.text = TextFactory(body=self.body)

    def test_GET(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            res.json(),
            [
                {
                    "id": 1,
                    "text": self.text.id,
                    "word": self.body,
                },
            ],
        )
