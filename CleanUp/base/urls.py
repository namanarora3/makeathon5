from django.urls import path
from . import views

urlpatterns = [
    path('',views.test,name="naman"),
    path('task',views.getTasks),
    path('task/<int:pk>/',views.getTask),
]