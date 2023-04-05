from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} - {self.project.name}'

#si quiero ver las tareas que le pertenecen a cierto projecto, en este caso, lo hago asi
#obtengo el project
#p=Project.objects.get(id=1)
#miro sus tareas relacionadas, lo pongo en minuscula pq es el nombre que le puso en la base de datos, es myapp_task, pero aqui nomas le pongo el task en minuscula por la base de datos
#p.task_set.all()
#guardar una tarea para ese project
#p.task_set.create(title="descargar IDE") #le puedo poner mas campos, pero para el ejemplo le dejo nomas el title