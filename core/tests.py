from django.test import TestCase, Client


class PagesTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_get_text_success(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "hi")
    
    def test_profile_fail(self):
        response = self.client.get("/profile")
        self.assertEqual(response.status_code, 404)

