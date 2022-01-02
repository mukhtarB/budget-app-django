from django.shortcuts import render, get_object_or_404

# models
from .models import Project

# Create your views here.


def project_list(request):
    return render(request, 'budget_app/project_list.html')


def project_detail(request, project_slug):
    # fetching the correct project

    # project = Project.objects.get(slug = project_slug)
    project = get_object_or_404(Project, slug=project_slug)

    context = {
        'project': project
    }
    return render(request, 'budget_app/project_detail.html', context)
