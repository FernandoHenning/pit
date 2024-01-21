from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=255, blank=True)
    image = models.ImageField(upload_to='project/logos/')
    repository_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', 'name')
        verbose_name_plural = 'Projects'
        verbose_name = 'Project'
