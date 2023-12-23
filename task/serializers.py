from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        allowed_methods = ['GET', 'POST', 'UPDATE', 'PUT', 'PATCH', 'DELETE']
