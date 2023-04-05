from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse
from .models import Project,Task
from .forms import CreateNewTask,CreateNewProject

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
    return render(request,'projects/projects.html',{
        'projects':projects
    })

def tasks(request):
    #task=get_object_or_404(Task,title=name)
    tasks=Task.objects.all()
    return render(request,'tasks/tasks.html',{
        'tasks':tasks
    })

def create_task(request):
    if request.method == 'GET':
      #le muestro la interfaz
      return render(request,'tasks/create_task.html',{
        'form':CreateNewTask()
    })
    else:
      #resivo los valores
      Task.objects.create(title=request.POST['title'],description=request.POST['description'],project_id=2)
      return redirect('tasks')

def create_project(request):
    if request.method=='GET':
      return render(request,'projects/create_project.html',{
        'form':CreateNewProject()
    })
    else:
       Project.objects.create(name=request.POST['name'])
       return redirect('projects')

def project_detail(request,id):
   project = get_object_or_404(Project,id=id)
   tasks = Task.objects.filter(project_id=id)
   return render(request,'projects/detail.html',{
      'project':project,
      'tasks':tasks
   })

def task_detail(request):
   pass