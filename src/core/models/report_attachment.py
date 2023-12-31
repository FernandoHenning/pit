from django.contrib.auth import get_user_model
from django.db import models


class ReportAttachment(models.Model):
    report = models.ForeignKey('core.Report', on_delete=models.CASCADE)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    file_url = models.URLField(blank=False, null=False)

    class Meta:
        ordering = ['-created_at']