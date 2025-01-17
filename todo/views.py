from rest_framework import generics, permissions
from .models import Todo
from .serializers import TodoSerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse
from .pagination import CustomPagination
from .permissions import IsOwner

class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination


    @extend_schema(
        description="Retrieve a list of all the user's tasks or create a new task.",
        responses={
            200: TodoSerializer(many=True),
            201: TodoSerializer,
            400: OpenApiResponse(description="Invalid data."),
        },
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        request=TodoSerializer,
        responses={
            201: TodoSerializer,
            400: OpenApiResponse(description="Invalid data."),
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]  # Add IsOwner

    @extend_schema(
        description="Retrieve, update, or delete a specific task.",
        responses={
            200: TodoSerializer,
            204: OpenApiResponse(description="Task deleted."),
            400: OpenApiResponse(description="Invalid data."),
            404: OpenApiResponse(description="Task not found."),
        },
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        request=TodoSerializer,
        responses={
            200: TodoSerializer,
            400: OpenApiResponse(description="Invalid data."),
            404: OpenApiResponse(description="Task not found."),
        },
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        responses={
            204: OpenApiResponse(description="Task deleted."),
            404: OpenApiResponse(description="Task not found."),
        },
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
