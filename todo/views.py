from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_todo_list(request):
    # return HttpResponse("Hello!")
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, "todo/todo_list.html", context)

def add_item(request):
    # A post request adds new item and returns user to updated template
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("get_todo_list")
    form = ItemForm()
    context = {
        'form': form
    }
        # A get request returns the template as is
    return render(request, "todo/add_item.html", context)

def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("get_todo_list")
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, "todo/edit_item.html", context)

def toggle_item(request, item_id):
    # If item is checked as done, toggle it so its not. Vice versa
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    # Take the user back to updated list
    return redirect("get_todo_list")

def delete_item(request, item_id):
    # If item is checked as done, toggle it so its not. Vice versa
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    # Take the user back to updated list
    return redirect("get_todo_list")