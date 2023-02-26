from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Tasks

from django.contrib.auth.models import User

@api_view(['GET'])
def getTasks(request):
    tasks = Tasks.objects.all()
    serialiser = TaskSerializer(tasks, many=True)
    return Response(serialiser.data)

@api_view(['GET'])
def getTask(request,pk):
    user = User.objects.filter(id=pk).first()
    task = Tasks.objects.filter(assigned=pk)
    serialiser = TaskSerializer(task, many=True)
    return Response(serialiser.data)

@api_view(['GET'])
def test(request):
    routes = {
        'naman':'na',
        'mait':'ma'
    }
    return Response(routes)