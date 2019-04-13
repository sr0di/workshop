from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from manager.constants import TaskState
from manager.serializers import TaskSerializer, BoardSerializer
from manager.models import Task, Board


class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @action(detail=False, methods=['GET'])
    def done_tasks(self, request):
        queryset = Task.objects.filter(state=TaskState.DONE)
        serializer = TaskSerializer(queryset, many=True)

        return Response(serializer.data)

    def filter_queryset(self, queryset):
        board  =self.request.GET.get('board')
        if board:
            queryset = queryset.filter(board=board)

        return queryset


class BoardViewSet(viewsets.ModelViewSet):

    serializer_class = BoardSerializer
    queryset = Board.objects.all()
