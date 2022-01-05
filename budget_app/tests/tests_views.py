import json
from django.test import TestCase, Client
from django.urls import reverse
from budget_app.models import (
    Category,
    Expense,
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
        self.add_url = reverse('add')

        self.project = Project.objects.create(
            name='project1',
            budget=7000
        )

        self.category = Category.objects.create(
            project=self.project,
            name='development_testing'
        )

        self.expense = Expense.objects.create(
            project=self.project,
            title='deletable expense',
            amount=700,
            category=self.category
        )

        return super().setUp()

    def test_project_list_GET(self) -> None:
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget_app/project_list.html')

    def test_project_detail_GET(self) -> None:
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget_app/project_detail.html')

    def test_project_detail_POST_add_expense(self) -> None:
        response = self.client.post(self.detail_url, {
            'title': 'expense1',
            'amount': 1000,
            'category': 'development_testing'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.project.expenses.first().title, 'expense1')

    def test_project_detail_POST_no_data(self) -> None:
        response = self.client.post(self.detail_url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.project.expenses.count(), 1)

    def test_project_detail_DELETE_deletes_expense(self) -> None:
        response = self.client.delete(self.detail_url, json.dumps({
            'id': 1
        }))

        self.assertEqual(response.status_code, 204)
        self.assertEqual(self.project.expenses.count(), 0)

    def test_project_detail_DELETE_no_id(self) -> None:
        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(self.project.expenses.count(), 1)

    def test_projectCreateView_GET(self) -> None:
        response = self.client.get(self.add_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget_app/add-project.html')

    def test_projectCreateView_POST(self) -> None:
        self.client.post(self.add_url, {
            'name': 'project2',
            'budget': 15000,
            'categoryString': 'design,development',
        })

        project2 = Project.objects.get(id=2)
        first_category = Category.objects.get(id=2)
        second_category = Category.objects.get(id=3)

        self.assertEqual(project2.name, 'project2')

        self.assertEqual(first_category.name, 'design')
        self.assertEqual(first_category.project, project2)

        self.assertEqual(second_category.name, 'development')
        self.assertEqual(first_category.project, project2)
