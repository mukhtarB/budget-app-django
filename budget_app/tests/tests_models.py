from django.test import TestCase
from ..models import (
    Category,
    Expense,
    Project
)


class TestModels(TestCase):

    def setUp(self) -> None:
        self.project = Project.objects.create(
            name='Project 1',
            budget=10000
        )
        return super().setUp()

    def test_project_assigns_slug_on_create(self) -> None:
        self.assertEqual(self.project.slug, 'project-1')

    def test_budget_left(self) -> None:
        category1 = Category.objects.create(
            project=self.project,
            name='development'
        )

        Expense.objects.create(
            project=self.project,
            title='expense1',
            amount=2000,
            category=category1
        )
        Expense.objects.create(
            project=self.project,
            title='expense2',
            amount=1000,
            category=category1
        )

        self.assertEqual(self.project.budget_left(), 7000)
