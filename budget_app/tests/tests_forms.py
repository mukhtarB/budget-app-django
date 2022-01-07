from django.test import SimpleTestCase
from ..forms import ExpenseForm


class TestForms(SimpleTestCase):

    def test_expense_form_valid_data(self) -> None:
        form = ExpenseForm(data={
            'title': 'expense1',
            'amount': 1000,
            'category': 'development'
        })

        self.assertTrue(form.is_valid())
