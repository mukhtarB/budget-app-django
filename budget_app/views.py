from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from django.http import HttpResponseRedirect

# models
from .models import Category, Expense, Project

# forms
from .forms import ExpenseForm

# Create your views here.


def project_list(request):
    return render(request, 'budget_app/project_list.html')


def project_detail(request, project_slug):
    # fetching the correct project

    # project = Project.objects.get(slug = project_slug)
    project = get_object_or_404(Project, slug=project_slug)

    if request.method == 'GET':
        category_list = Category.objects.filter(project=project)

        context = {
            'project': project,
            'expense_list': project.expenses.all(),
            'category_list': category_list
        }
        return render(request, 'budget_app/project_detail.html', context)

    elif request.method == 'POST':
        # process the forms
        form = ExpenseForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            amount = form.cleaned_data['amount']
            category_name = form.cleaned_data['category']

            category = get_object_or_404(Category, project=project, name=category_name)

            Expense.objects.create(
                project=project,
                title=title,
                amount=amount,
                category=category,
            ).save()
        # pass

    return HttpResponseRedirect(project_slug)


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'budget_app/add-project.html'
    fields = ('name', 'budget')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        categories = self.request.POST['categoryString'].split(',')

        for category in categories:
            Category.objects.create(
                project=Project.objects.get(id=self.object.id),
                name=category
            ).save()

        # return HttpResponseRedirect(self.get_success_url())
        return super().form_valid(form)
