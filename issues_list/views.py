from django.shortcuts import render,  HttpResponse
from .models import Item
# Create your views here.

def get_issues_list(request):
    results=Item.objects.all()
    return render(request, "issues_list.html", {'items': results}) #'ordering': ordering})