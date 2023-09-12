from rest_framework.views import APIView

from .models import Tasks
from .serializers import TasksSerializer
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.exceptions import PermissionDenied


class TasksView(APIView):
    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Tasks.objects.filter(Q(assigned_to=user) | Q(user=user))

    def update(self, request, *args, **kwargs):
        tasks_id = kwargs['pk']
        try:
            instance = get_object_or_404(Tasks, pk=tasks_id)
        except Tasks.DoesNotExist:
            return Response({'error': 'Tasks not found.'}, status=status.HTTP_404_NOT_FOUND)

        if request.user != instance.user and request.user not in instance.assigned_to.all():
            raise PermissionDenied('You are not authorized to update this task.')

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
