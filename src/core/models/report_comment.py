from django.contrib.auth import get_user_model
from django.db import models


class ReportComment(models.Model):
    report = models.ForeignKey('core.Report', on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
