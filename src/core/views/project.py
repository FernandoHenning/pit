from django.views.generic import ListView

from ..models import Project


class ProjectList(ListView):
    model = Project
    context_object_name = 'projects'
