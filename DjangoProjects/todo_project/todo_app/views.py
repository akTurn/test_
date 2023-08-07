from rest_framework import views, response,generics
from .models import Todo
from .serializers import TodoSerializer

class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoReset(views.APIView):
    def post(self, request, format=None):
        # Reset all todos to not completed
        todos = Todo.objects.all()
        for todo in todos:
            todo.completed = False
            todo.save()

        serializer = TodoSerializer(todos, many=True)
        return response.Response(serializer.data)
