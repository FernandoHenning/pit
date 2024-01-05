from django.test import TestCase
from unittest.mock import patch, MagicMock
from django.utils import timezone
from ..models import Project, Version, Report, Type, Priority, Status, Resolution
from django.contrib.auth import get_user_model


class ReportModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='UserName', password='password1234')
        self.project = Project.objects.create(name='Test Project')
        self.version = Version.objects.create(name='1.0', version_number='1.0', project=self.project)
        self.report_data = {
            'title': 'Test Report',
            'description': 'Test Description',
            'type': Type.FUNCTIONAL,
            'priority': Priority.NORMAL,
            'status': Status.CLOSED,
            'resolution': Resolution.FIXED,
            'fix_version': self.version,
            'project': self.project,
            'author': self.user
        }

    @patch('django.utils.timezone.now')
    def test_report_creation(self, mock_now: MagicMock) -> None:
        mock_now.return_value = timezone.datetime(2024, 1, 4, 12, 0, 0, tzinfo=timezone.utc)
        report = Report.objects.create(**self.report_data)

        self.assertEqual(report.title, self.report_data['title'])
        self.assertEqual(report.description, self.report_data['description'])
        self.assertEqual(report.type, self.report_data['type'])
        self.assertEqual(report.priority, self.report_data['priority'])
        self.assertEqual(report.status, self.report_data['status'])
        self.assertEqual(report.resolution, self.report_data['resolution'])
        self.assertEqual(report.fix_version, self.report_data['fix_version'])
        self.assertEqual(report.project, self.project)
        self.assertEqual(report.author, self.user)
        self.assertEqual(report.created_at, timezone.datetime(2024, 1, 4, 12, 0, 0, tzinfo=timezone.utc))

    def test_updated_at_auto_now(self):
        report = Report.objects.create(**self.report_data)
        original_updated_at = report.updated_at

        report.title = 'Updated Title'
        report.save()

        self.assertTrue(report.updated_at > original_updated_at)

    def test_report_ordering(self):
        Report.objects.create(**self.report_data)

        later_report_data = self.report_data.copy()
        later_report_data['title'] = 'Another Report'
        later_report_data['created_at'] = timezone.now() + timezone.timedelta(days=1)
        Report.objects.create(**later_report_data)

        reports = Report.objects.all()
        self.assertEqual(reports[0].title, 'Another Report')
        self.assertEqual(reports[1].title, 'Test Report')
