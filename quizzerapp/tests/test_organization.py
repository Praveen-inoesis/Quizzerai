# tests/test_organization.py

from rest_framework import status
from rest_framework.test import APITestCase
from quizzerapp.models.organization import Organization

class OrganizationDetailTests(APITestCase):
    def setUp(self):
        from quizzerapp.models.organization import Organization  # Local import
        self.organization = Organization.objects.create(
            organization_name="Test Organization",
            domain_name="test.org",
            admin_email="admin@test.org"
        )
        self.url = f'/api/organizations/{self.organization.organization_id}/'


    def test_get_organization(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['organization_name'], self.organization.organization_name)

    def test_patch_organization(self):
        data = {'organization_name': 'Updated Organization'}
        response = self.client.patch(self.url, data)
        self.organization.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.organization.organization_name, 'Updated Organization')

    def test_delete_organization(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Organization.objects.filter(pk=self.organization.pk).exists())
