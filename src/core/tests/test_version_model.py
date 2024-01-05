from django.test import TestCase
from django.utils import timezone
from unittest.mock import patch
from datetime import datetime
from core.models import Project, Version


class VersionModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            name=f"test_project-{datetime.now()}",
            description="test_project",
            repository="https://github.com/test/test-project")

        self.version_data = {
            'name': 'Test Version',
            'version_number': '1.0',
            'status': True,
            'version_link': 'https://example.com',
            'project': self.project
        }

    @patch('django.utils.timezone.now')
    def test_version_creation(self, mock_now):
        mock_now.return_value = timezone.datetime(2024, 1, 4, 12, 0, 0, tzinfo=timezone.utc)
        version = Version.objects.create(**self.version_data)

        self.assertTrue(isinstance(version, Version))
        self.assertEqual(version.name, 'Test Version')
        self.assertEqual(version.version_number, '1.0')
        self.assertTrue(version.status)
        self.assertEqual(version.version_link, 'https://example.com')
        self.assertEqual(version.project, self.project)
        self.assertEqual(version.created_at, timezone.datetime(2024, 1, 4, 12, 0, 0, tzinfo=timezone.utc))

    @patch('django.utils.timezone.now')
    def test_created_at_auto_now_add(self, mock_now):
        mock_now.return_value = timezone.datetime(2024, 1, 4, 12, 0, 0, tzinfo=timezone.utc)
        version = Version.objects.create(**self.version_data)

        self.assertTrue(version.created_at <= timezone.datetime(2024, 1, 4, 12, 0, 0, tzinfo=timezone.utc))

    @patch('django.utils.timezone.now')
    def test_version_ordering(self, mock_now):
        mock_now.return_value = timezone.datetime(2024, 1, 4, 12, 0, 0, tzinfo=timezone.utc)
        Version.objects.create(**self.version_data)

        later_version_data = self.version_data.copy()
        later_version_data['version_number'] = '2.0'
        mock_now.return_value = timezone.datetime(2024, 1, 5, 12, 0, 0, tzinfo=timezone.utc)
        Version.objects.create(**later_version_data)

        versions = Version.objects.all()
        self.assertEqual(versions[0].version_number, '2.0')
        self.assertEqual(versions[1].version_number, '1.0')

    @patch('django.utils.timezone.now')
    def test_unique_version_number(self, mock_now):
        mock_now.return_value = timezone.datetime(2024, 1, 4, 12, 0, 0, tzinfo=timezone.utc)
        Version.objects.create(**self.version_data)

        duplicate_version_data = self.version_data.copy()
        with self.assertRaises(Exception):
            # Attempting to create a version with the same version_number should raise an exception
            Version.objects.create(**duplicate_version_data)
