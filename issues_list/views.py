from django.shortcuts import render,  HttpResponse, redirect
from .models import Item
from .forms import ItemForm
from django.contrib.auth.models import User, Group, Permission, ContentType
# Create your views here.

def get_issues_list(request):
    """ Render the ticket list """
    results=Item.objects.all()
    return render(request, "issues_list.html", {'items': results})#,'ordering': ordering})

def create_an_item(request):
    """ Present a blank form to be filled in """
    if request.method == "POST":
        #create new form
        form = ItemForm(request.POST, request.FILES)
        #django checks if form is valid and saves if so
        if form.is_valid():
            form.save()
            return redirect(get_issues_list)
    #if not a post request return an empty form
    else:
        form = ItemForm()

    return render(request, "itemform.html", {'form': form})