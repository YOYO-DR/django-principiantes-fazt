from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import Project,Task

def index(request):
    title='Django Course!!'
    return render(request,'index.html',{
        'title':title
    })

def about(request):
    username = 'yoiner'
    return render(request,'about.html',{
                  'username':username}
                  )

def hello(request,username):
    return HttpResponse(f"<h1>Hello {username}</h1>")


def projects(request):
    #con .values() es para traer todos los valores y list para poderlo pasar como Json 
    #projects=list(Project.objects.values())
    projects=Project.objects.all()
    return render(request,'projects.html',{
        'projects':projects
    })

def tasks(request):
    #task=get_object_or_404(Task,title=name)
    tasks=Task.objects.all()
    return render(request,'tasks.html',{
        'tasks':tasks
    })
