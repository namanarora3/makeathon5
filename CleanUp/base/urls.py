from django.urls import path
from . import views

urlpatterns = [
    path('',views.test,name="naman"),
    path('tasks/',views.getTasks, name='tasks_all'), 
]