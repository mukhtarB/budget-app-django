from django.test import TestCase
from ..models import (
    Project
)


class TestModels(TestCase):
    def setUp(self) -> None:
        self.project = Project.objects.create(
            name='project-1',
            budget=7000
        )
        return super().setUp()
