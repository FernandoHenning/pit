from django.views.generic import ListView, FormView

from ..models import Project
from ..forms import ProjectForm


class ProjectList(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'project/project-list.html'


class ProjectCreate(FormView):
    form_class = ProjectForm
    success_url = '/projects/'
    template_name = 'project/create-project.html'

    def form_valid(self, form):
        project = form.save(commit=False)
        
        project.save()
        return super(ProjectCreate, self).form_valid(form)


