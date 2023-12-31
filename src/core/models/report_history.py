from django.db import models


class ReportHistory(models.Model):
    report = models.ForeignKey('core.Report', on_delete=models.CASCADE)
    updated_by = models.ForeignKey('core.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    field = models.CharField(max_length=50, blank=False, null=False)
    old_value = models.CharField(null=False, blank=False, max_length=100)
    new_value = models.CharField(null=False, blank=False, max_length=100)

    class Meta:
        ordering = ('-created_at',)
