from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='home'),
    path('about/',about,name='about'),
    path('hello/<str:username>/',hello),
    path('projects/',projects,name='projects'),
    path('projects/<int:id>/',project_detail,name='project_detail'),
    path('tasks/',tasks,name='tasks'),
    path('create_task/',create_task,name='create_task'),
    path('create_project/',create_project,name='create_project'),
]
