from django.test import TestCase

# Create your tests here.
class TestApi(TestCase):
    def test_api_root(self):
        response = self.client.get('/api/task/')
        self.assertEqual(response.status_code, 401)