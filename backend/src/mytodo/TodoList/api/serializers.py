from rest_framework.serializers import ModelSerializer
from TodoList.models import Todo

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields ="__all__"