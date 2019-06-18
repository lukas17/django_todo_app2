from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm

from .models import Todo3
from .forms import TodoForm3

from django.views.generic import TemplateView

def index(request):
    todo_list = Todo.objects.order_by('id')

    form = TodoForm()

    context = {'todo_list' : todo_list, 'form' : form}

    return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')

class AboutView(TemplateView):
    template_name = "about.html"

# App3 portion

def app3(request):
    todo_list = Todo3.objects.order_by('id')

    form = TodoForm3()

    context = {'todo_list' : todo_list, 'form' : form}

    return render(request, 'todo/app3.html', context)

def addTodo3(request):
    form = TodoForm3(request.POST)

    if form.is_valid():
        new_todo = Todo3(text=request.POST['text'])
        new_todo.save()

    return redirect('app3')

def completeTodo3(request, todo_id):
    todo = Todo3.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('app3')

def deleteCompleted3(request):
    Todo3.objects.filter(complete__exact=True).delete()

    return redirect('app3')

def deleteAll3(request):
    Todo3.objects.all().delete()

    return redirect('app3')
