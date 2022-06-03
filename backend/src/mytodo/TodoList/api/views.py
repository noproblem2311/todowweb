from rest_framework.viewsets import ModelViewSet
from .serializers import TodoSerializer
from TodoList.models import Todo


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
   