from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import project_list


class TestUrls(SimpleTestCase):

    def test_list_url_resolves(self):
        url = reverse('list')
        self.assertEqual(resolve(url).func, project_list)
