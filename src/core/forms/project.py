from django.forms import ModelForm
from core.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'image', 'repository_url']
