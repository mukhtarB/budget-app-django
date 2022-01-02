from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

# models
from .models import Project
# Create your views here.

def project_list(request):
    return render(request, 'budget_app/project_list.html')


def project_detail(request, project_slug):
    # fetching the correct project

    # project = Project.objects.get(slug = project_slug)
    project =  get_object_or_404(Project, slug=project_slug)

    context = {
        'project': project,
        'expense_list': project.expenses.all()
    }
    return render(request, 'budget_app/project_detail.html', context)


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'budget_app/add-project.html'
    fields = ('name', 'budget')
