from django.contrib.auth import get_user_model
from django.db import models
from .choices import Type, Priority, Status, Resolution


class Report(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.IntegerField(choices=Type.choices, default=Type.FUNCTIONAL)
    priority = models.IntegerField(choices=Priority.choices, default=Priority.NORMAL)
    status = models.IntegerField(choices=Status.choices, default=Status.OPEN)
    resolution = models.IntegerField(choices=Resolution.choices, blank=True, null=True)
    fix_version = models.ForeignKey('core.Version', on_delete=models.SET_NULL, blank=True, null=True)
    affected_versions = models.ManyToManyField('core.Version', related_name='affected_versions')
    project = models.ForeignKey('core.Project', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Project Report'
        verbose_name_plural = 'Project Reports'


class ReportAttachment(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    file_url = models.URLField(blank=False, null=False)

    class Meta:
        ordering = ['-created_at']


class ReportComment(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)


class ReportHistory(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    field = models.CharField(max_length=50, blank=False, null=False)
    old_value = models.CharField(null=False, blank=False, max_length=100)
    new_value = models.CharField(null=False, blank=False, max_length=100)

    class Meta:
        ordering = ('-created_at',)
