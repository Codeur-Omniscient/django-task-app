from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from tasks.models import Task



class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    
    def test_task_list(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
    
    def test_task_create(self):
        url = reverse('task-create')
        data = {
            "title": "Learn DjangoREST",
            "owner": self.user.username,
            "description":"Become more skilled in that framework",
            "status":"todo",
            "priority":"low"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, "Learn DjangoREST")
        self.assertEqual(Task.objects.get().owner.username, "testuser")

    def test_task_detail(self):
        task = Task.objects.create(
            title="Test Task",
            owner=self.user,
            description="Test Description",
            status="todo",
            priority="low"
        )
        url = reverse('task-detail', kwargs={'pk': task.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Task")
        self.assertEqual(response.data['owner'], self.user.username)
    
    def test_task_update(self):
        task = Task.objects.create(
            title="Test Task",
            owner=self.user,
            description="Test Description",
            status="todo",
            priority="low"
        )
        url = reverse('task-detail', kwargs={'pk': task.pk})
        data = {
            "title": "Updated Task",
            "owner": self.user.username,
            "description": "Updated Description",
            "status": "in_progress",
            "priority": "medium"
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Task')
    
    def test_task_delete(self):
        task = Task.objects.create(
            title="Test Task",
            owner=self.user,
            description="Test Description",
            status="todo",
            priority="low"
        )
        url = reverse('task-detail', kwargs={'pk': task.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)




