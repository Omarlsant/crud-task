from rest_framework import status
from rest_framework.test import APITestCase

from .models import Task


class TaskApiTests(APITestCase):
    endpoint = '/tasks/api/v1/tasks/'

    def test_root_explains_available_resources(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['api'], 'http://testserver/tasks/api/v1/tasks/')
        self.assertEqual(response.json()['docs'], 'http://testserver/tasks/docs/')

    def test_list_returns_tasks_in_creation_order(self):
        first = Task.objects.create(title='Primera tarea')
        second = Task.objects.create(title='Segunda tarea')

        response = self.client.get(self.endpoint)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([task['id'] for task in response.data], [second.id, first.id])

    def test_create_strips_title_and_uses_default_done_value(self):
        response = self.client.post(
            self.endpoint,
            {'title': '  Preparar entrega  ', 'description': 'Revisar cambios'},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Preparar entrega')
        self.assertFalse(response.data['done'])
        self.assertTrue(Task.objects.filter(title='Preparar entrega').exists())

    def test_create_rejects_blank_title(self):
        response = self.client.post(self.endpoint, {'title': '   '}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data)

    def test_update_and_delete_task(self):
        task = Task.objects.create(title='Pendiente')

        update_response = self.client.patch(
            f'{self.endpoint}{task.id}/',
            {'done': True},
            format='json',
        )
        delete_response = self.client.delete(f'{self.endpoint}{task.id}/')

        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertTrue(update_response.data['done'])
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=task.id).exists())
