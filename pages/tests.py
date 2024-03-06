from django.test import TestCase, SimpleTestCase
from django.urls import reverse

class HomepageTest(SimpleTestCase):
    def test_url_exit_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class AboutpageTest(SimpleTestCase):
    def test_url_exit_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)