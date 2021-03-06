from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
import json

# models
from .models import Category, Expense, Project

# forms
from .forms import ExpenseForm

# Create your views here.


def project_list(request):
    project_list = Project.objects.all()
    context = {
        'project_list': project_list
    }
    return render(request, 'budget_app/project_list.html', context)


def project_detail(request, project_slug):
    # fetching the correct project

    # project = Project.objects.get(slug = project_slug)
    project = get_object_or_404(Project, slug=project_slug)
    form = ExpenseForm()

    if request.method == 'GET':
        category_list = Category.objects.filter(project=project)

        context = {
            'project': project,
            'expense_list': project.expenses.all(),
            'category_list': category_list,
            'form': form
        }
        return render(request, 'budget_app/project_detail.html', context)

    elif request.method == 'POST':
        # process the forms: manually in templates

        form = ExpenseForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            amount = form.cleaned_data['amount']
            category_name = form.cleaned_data['category']

            category = get_object_or_404(
                Category, project=project, name=category_name)

            Expense.objects.create(
                project=project,
                title=title,
                amount=amount,
                category=category
            ).save()

    elif request.method == 'DELETE':
        try:
            id = json.loads(request.body)['id']
            expense = get_object_or_404(Expense, id=id)
            expense.delete()
        except:
            return HttpResponse(status=404)
        return HttpResponse(status=204)

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

        return super().form_valid(form)
