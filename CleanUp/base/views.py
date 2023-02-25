from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Tasks

@api_view(['GET'])
def test(request):
    routes = {
        'naman':'na',
        'mait':'ma'
    }
    return Response(routes)

@api_view(['GET'])
def getTasks(request):
    tasks = Tasks.objects.all()
    serialiser = TaskSerializer(tasks, many=True)
    return Response(serialiser.data)