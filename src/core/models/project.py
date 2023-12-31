from django.db import models

from core.constants import DEFAULT_PROJECT_IMAGE


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    description = models.TextField(blank=True)
    repository = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image_link = models.URLField(blank=False, null=False, default=DEFAULT_PROJECT_IMAGE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
