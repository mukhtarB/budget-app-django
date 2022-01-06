from django.test import TestCase
from ..models import (
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
