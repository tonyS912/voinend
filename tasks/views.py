from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status

from .models import Tasks, Category
from .serializers import TasksSerializer, CategorySerializer


class TasksView(APIView):
    queryset = Tasks.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        tasks_items = Tasks.objects.all()
        serializer_class = TasksSerializer(tasks_items, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        serializer_class = TasksSerializer(data=self.request.data)
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()
        return Response(serializer_class.data, status=status.HTTP_201_CREATED)


class TasksDetailView(APIView):
    queryset = Tasks.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, id):
        tasks = Tasks.objects.get(id=id)
        serializer_class = TasksSerializer(tasks)
        return Response(serializer_class.data)

    def put(self, request, id):
        tasks = Tasks.objects.get(id=id)
        serializer_class = TasksSerializer(tasks, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        Tasks.objects.get(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryView(APIView):
    queryset = Category.objects.all()

    def get(self, request):
        tasks_items = Category.objects.all()
        serializer_class = CategorySerializer(tasks_items, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        serializer_class = CategorySerializer(data=self.request.data)
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()
        return Response(serializer_class.data, status=status.HTTP_201_CREATED)


class CategoryDetailView(APIView):
    queryset = Category.objects.all()

    def get(self, request, id):
        tasks = Category.objects.get(id=id)
        serializer_class = CategorySerializer(tasks)
        return Response(serializer_class.data)

    def put(self, request, id):
        tasks = Category.objects.get(id=id)
        serializer_class = CategorySerializer(tasks, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        Category.objects.get(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)