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
                "words": [
                    {
                        "id": 1,
                        "name": self.text.word_set.first().name,
                    },
                    {
                        "id": 2,
                        "name": self.text.word_set.last().name,
                    },
                ],
            },
        )
