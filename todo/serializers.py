from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    deadline = serializers.DateTimeField(
        required=False,
        allow_null=True,
        help_text="Deadline for the task (in ISO 8601 format)."
    )

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed', 'deadline', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
