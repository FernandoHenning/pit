from django.urls import path
from core.views import ProjectList, ProjectCreate

urlpatterns = [
    path('', ProjectList.as_view(), name='project-list'),
    path('create', ProjectCreate.as_view(), name='project-create')
]
