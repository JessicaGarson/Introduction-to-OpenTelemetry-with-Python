from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDoItem
from .forms import ToDoForm

def index(request):
    items = ToDoItem.objects.all()
    return render(request, 'todo/index.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ToDoForm()
    return render(request, 'todo/add_item.html', {'form': form})

def delete_item(request, item_id):
    item = get_object_or_404(ToDoItem, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
