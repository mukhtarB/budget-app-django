from django import forms


CHOICES = [
    ('default', 'Select a Category'),
    ('design', 'Design'),
    ('development', 'Development'),
]


class ExpenseForm(forms.Form):
    title = forms.CharField(help_text="Enter your title")
    amount = forms.IntegerField()
    category = forms.CharField(
        label='Category:?', widget=forms.Select(choices=CHOICES), initial='default')
