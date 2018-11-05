from django.shortcuts import render,  HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def get_issues_list(request):
    """ Render the ticket list """
    item_list=Item.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(item_list, 10)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)
    return render(request, "issues_list.html", {'items': items})

def create_an_item(request):
    """ Present a blank form to be filled in """
    if request.method == "POST":
        #create new form
        form = ItemForm(request.POST, request.FILES)
        #django checks if form is valid and saves if so
        if form.is_valid():
            if request.user.is_authenticated():
                form = form.save(commit=False)
                form.user=request.user
                form.save()
                return redirect(get_issues_list)
    #if not a post request return an empty form
    else:
        form = ItemForm()
    return render(request, "itemform.html", {'form': form})
#get item where primary key = id
def edit_an_item(request, id):
    """ Return an existing form for edit """
    item = get_object_or_404(Item, pk=id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_issues_list)
    else:
        #item is the instance that we want to construct the object from
        form = ItemForm(instance=item)
    return render(request, "editform.html", {'form': form})
