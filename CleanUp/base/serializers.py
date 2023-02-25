from rest_framework.serializers import ModelSerializer
from .models import Tasks

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id','assigned','name','category','location','created','image','approved','assigned.username']