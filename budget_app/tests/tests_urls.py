from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import (
    ProjectCreateView,
    project_detail,
    project_list
)


class TestUrls(SimpleTestCase):

    def test_list_url_resolves(self):
        url = reverse('list')
        self.assertEqual(resolve(url).func, project_list)

    def test_detail_url_resolves(self):
        url = reverse('detail', args=['random-slug'])
        self.assertEqual(resolve(url).func, project_detail)

    def test_add_project_url_resolves(self):
        url = reverse('add')
        self.assertEqual(resolve(url).func.view_class, ProjectCreateView)
