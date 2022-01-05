from django.http import response
from django.test import TestCase, Client, client
from django.urls import reverse
from budget_app.models import (
    Category,
    Project,
)
from budget_app.views import project_list

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

        self.category = Category.objects.create(
            project=self.project,
            name='development_testing'
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

    def test_project_detail_POST_add_expense(self):
        response = self.client.post(self.detail_url, {
            'title': 'expense1',
            'amount': 1000,
            'category': 'development_testing'
        })

        print(self.project.expenses)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.project.expenses.first().title, 'expense1')
