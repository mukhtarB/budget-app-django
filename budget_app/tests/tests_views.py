from django.http import response
from django.test import TestCase, Client, client
from django.urls import reverse
# from budget_app.models import ()

# setup codes
# test codes
# assertion codes


class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.list_url = reverse('list')
        return super().setUp()

    def test_project_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget_app/project_list.html')
