from django.db import models


class Version(models.Model):
    name = models.CharField(max_length=100, blank=True)
    version_number = models.CharField(max_length=10, unique=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    version_link = models.URLField(blank=True)
    project = models.ForeignKey('core.Project', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at', '-version_number')
        verbose_name = 'Project Version'
        verbose_name_plural = 'Project Versions'
