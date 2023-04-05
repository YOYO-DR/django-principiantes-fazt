from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label='Titulo de tarea', max_length=200, widget=forms.TextInput(attrs={'class': 'input'})) #aqui le digo que el widget va a ser de textinput y le paso los atributos que quiero ponerle
    description = forms.CharField(label='Descripcion de la tarea', widget=forms.Textarea(attrs={'class': 'input'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label='Nombre del proyecto',max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))