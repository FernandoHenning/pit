from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    repository = models.URLField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image_link = models.URLField(blank=False, null=False)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
