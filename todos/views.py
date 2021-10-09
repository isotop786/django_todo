from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm


# Create your views here.

def home(request):
    return HttpResponse('<h2>Welcome to Djanog Todo app</h2>')

def list_todo(request):
    todo = Todo.objects.all().order_by('id').reverse()
    context = {
        "todos" : todo
    }
    
    return render(request,"todos/list.html",context)

def add_todo(request):
    
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        
        Todo.objects.create(
            title=title,
            description = description
        )
        
        return redirect('/todos/')
       # print(title, description)
    
    
    form = TodoForm
    context ={
        "form": form
    }
    
    return render(request,"todos/add_todo.html",context)
    
    

# update todo 

def update_todo(request,pk):
    todo = Todo.objects.get(id=pk)
    
    # post method
    if request.method == "POST":
        
        title = request.POST['title']
        descripton = request.POST['description']
        todo.title = title
        todo.description = descripton
        todo.save()
        
        return redirect('/todos/')
    
    
    
    
    # get method
    context ={
        "todo" : todo
    }
    
    return render(request,"todos/update.html",context)

    
# delete todo 

def delete_todo(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    
    return redirect('/todos/')
    