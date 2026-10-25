from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'done')

    def validate_title(self, value):
        title = value.strip()
        if not title:
            raise serializers.ValidationError('El título no puede estar vacío.')
        return title