from django.contrib.auth import get_user_model
from django.db import models


class Report(models.Model):
    class Type(models.IntegerChoices):
        FUNCTIONAL = 1, "Functional Issue"
        INTERFACE_PROBLEM = 2, "Interface Problem"
        PERFORMANCE_PROBLEM = 3, "Performance Problem"
        COMPATIBILITY_PROBLEM = 4, "Compatibility Problem"
        SECURITY_VULNERABILITY = 5, "Security Vulnerability"
        USABILITY_PROBLEM = 6, "Usability Problem"
        NETWORK_CONNECTIVITY = 7, "Network Connectivity"
        CRASH_OR_FREEZE = 8, "Crash or freeze"
        ACCESSIBILITY_PROBLEM = 9, "Accessibility Problem"
        OTHER_PROBLEM = 10, "Other"

    class Priority(models.IntegerChoices):
        BLOCKER = 1, "Blocker"
        CRITICAL = 2, "Critical"
        IMPORTANT = 3, "Important"
        NORMAL = 4, "Normal"
        HIGH = 5, "High"
        MEDIUM = 6, "Medium"
        MINOR = 7, "Minor"

    class Status(models.IntegerChoices):
        OPEN = 1, "Open"
        IN_PROGRESS = 2, "In Progress"
        RESOLVED = 3, "Resolved"
        CLOSED = 4, "Closed"
        TO_DO = 5, "To do"
        POSTPONED = 6, "Postponed"

    class Resolution(models.IntegerChoices):
        FIXED = 1, "Fixed"
        WONT_FIX = 2, "Won't Fix"
        DUPLICATE = 3, "Duplicate"
        INCOMPLETE = 4, "Incomplete"
        INTENDED = 5, "Intended"
        CANNOT_REPRODUCE = 6, "Can't Reproduce"
        INVALID = 7, "Invalid"
        AWAITING_RESPONSE = 8, "Awaiting Response"
        DONE = 9, "Done"
        WONT_DO = 10, "Won't Do"
        DECLINED = 11, "Declined"

    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.IntegerField(choices=Type.choices, default=Type.FUNCTIONAL)
    priority = models.IntegerField(choices=Priority.choices, default=Priority.NORMAL)
    status = models.IntegerField(choices=Status.choices, default=Status.OPEN)
    resolution = models.IntegerField(choices=Resolution.choices, blank=True, null=True)
    fix_version = models.ForeignKey('core.Version', on_delete=models.SET_NULL, blank=True, null=True)
    affected_versions = models.ManyToManyField('core.Version')
    project = models.ForeignKey('core.Project', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Project Report'
        verbose_name_plural = 'Project Reports'
