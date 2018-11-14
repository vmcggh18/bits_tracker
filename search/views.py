from django.shortcuts import render
from issues_list.models import Item

def do_search(request):
    """ Create do_search method """
    items = Item.objects.filter(name__icontains=request.GET['q'])
    return render(request, "issues_list.html", { 'items' : items })

