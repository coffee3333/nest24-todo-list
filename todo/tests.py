from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from .models import Todo
from .serializers import TodoSerializer
from django.utils import timezone
import datetime

class TodoSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.todo = Todo.objects.create(
            user=self.user,
            title='Test Task',
            description='This is a test task.',
            deadline=timezone.now() + datetime.timedelta(days=1)
        )

    def test_todo_serializer(self):
        serializer = TodoSerializer(instance=self.todo)
        data = serializer.data
        self.assertEqual(data['id'], self.todo.id)
        self.assertEqual(data['title'], self.todo.title)
        self.assertEqual(data['description'], self.todo.description)
        self.assertEqual(data['completed'], self.todo.completed)
        self.assertEqual(data['deadline'], self.todo.deadline.isoformat())
        self.assertIsNotNone(data['created_at'])
        self.assertIsNotNone(data['updated_at'])
