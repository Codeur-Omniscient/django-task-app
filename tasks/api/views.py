from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from tasks.api.serializers import TaskSerializers
from tasks.models import Task




class UserTaskView(generics.ListAPIView):
    serializer_class = TaskSerializers
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    
class TaskCreateView(generics.CreateAPIView):
    
    serializer_class = TaskSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializers
    permission_classes = [IsAuthenticated]

    queryset = Task.objects.all()

