from django.urls import path
from .views import TodoListCreateView, TodoRetrieveUpdateDestroyView

urlpatterns = [
    path('', TodoListCreateView.as_view(), name='todo-list-create'),
    path('<int:pk>/', TodoRetrieveUpdateDestroyView.as_view(), name='todo-detail'),
]
