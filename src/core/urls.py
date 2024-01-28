from django.urls import path
from core.views import ProjectList, ProjectCreate, UpdateProjectVIew

urlpatterns = [
    path('', ProjectList.as_view(), name='project-list'),
    path('create', ProjectCreate.as_view(), name='project-create'),
    path('<int:pk>/edit/', UpdateProjectVIew.as_view(), name='project-edit')
]
