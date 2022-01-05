from django.http import response
from django.test import TestCase, Client, client
from django.urls import reverse
from budget_app.models import (
    Project,
)

# setup codes
# test codes
# assertion codes


class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.list_url = reverse('list')
        self.detail_url = reverse('detail', args=['project1'])

        self.project = Project.objects.create(
            name='project1',
            budget=7000
        )

        return super().setUp()

    def test_project_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget_app/project_list.html')

    def test_project_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget_app/project_detail.html')
