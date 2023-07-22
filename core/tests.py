from django.test import TestCase, Client
from django.urls import reverse

class ContactViewsetTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_returns_success(self):
        response = self.client.post(reverse('contact-list'), {
            'interest': 'Product Inquiry',
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'Interested in your product. Please contact.',
        })

        # Check that the response has an HTTP status code of 200
        self.assertEqual(response.status_code, 200)

        # Check that the response content is as expected
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {"status":"success","content":"message sent successfully"}
        )
