from django.test import TestCase
from django.utils import timezone
from unittest.mock import patch, MagicMock
from ..models import Project


class ProjectModelTest(TestCase):

    def setUp(self):
        self.project_data = {
            'name': 'Test Project',
            'description': 'Test Description',
            'repository': 'https://github.com/test',
            'image_link': 'https://cdn.test.com/test'
        }

    @patch('django.utils.timezone.now')
    def test_project_creation(self, mock_now):
        mock_now.return_value = timezone.datetime(2024, 1, 4, 12, 0, 0, tzinfo=timezone.utc)
        project = Project.objects.create(**self.project_data)

        self.assertTrue(isinstance(project, Project))
        self.assertEqual(project.name, self.project_data['name'])
        self.assertEqual(project.description, self.project_data['description'])
        self.assertEqual(project.repository, self.project_data['repository'])
        self.assertEqual(project.image_link, self.project_data['image_link'])
        self.assertEqual(project.created_at, timezone.datetime(2024, 1, 4, 12, 0, 0, tzinfo=timezone.utc))

    def test_project_ordering(self):
        Project.objects.create(**self.project_data)

        later_project_data = self.project_data.copy()
        later_project_data['name'] = 'Another Project'
        Project.objects.create(**later_project_data)

        projects = Project.objects.all()
        self.assertEqual(projects[0].name, later_project_data['name'])
        self.assertEqual(projects[1].name, self.project_data['name'])

    @patch('django.utils.timezone.now')
    def test_unique_name(self, mock_now):
        mock_now.return_value = timezone.datetime(2024, 1, 4, 12, 0, 0, tzinfo=timezone.utc)
        Project.objects.create(**self.project_data)

        duplicate_version_data = self.project_data.copy()
        with self.assertRaises(Exception):
            # Attempting to create a project with the same name should raise an exception
            Project.objects.create(**duplicate_version_data)